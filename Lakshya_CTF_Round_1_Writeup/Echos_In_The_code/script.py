from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time
import os

# Set the path for your GeckoDriver (Firefox driver)
gecko_driver_path = '/path/to/geckodriver/'  # Update with your actual path
download_dir = '/path/to/download/dir'  # Update with your desired download location
file_list_path = './wordlist.txt'  # Path to the .txt file containing file names

# Set Firefox options to handle download
firefox_options = webdriver.FirefoxOptions()
firefox_options.set_preference("browser.download.folderList", 2)  # Custom download directory
firefox_options.set_preference("browser.download.dir", download_dir)  # Set the download directory
firefox_options.set_preference("browser.download.useDownloadDir", True)  # Use default download directory
firefox_options.set_preference("browser.download.prompt_for_download", False)  # Do not show download prompt
firefox_options.set_preference("browser.helperApps.neverAsk.saveToDisk", "*/*")  # Allow all file types to be downloaded

service = Service(gecko_driver_path)

# Create a new WebDriver instance
driver = webdriver.Firefox(service=service, options=firefox_options)

# Open the main website
driver.get("https://lakshyactf-web2.onrender.com/")  # Replace with your URL

# Read file names from the .txt file
def read_file_names(file_path):
    with open(file_path, 'r') as file:
        # Strip any extra spaces or newlines and return the list of file names
        return [line.strip() for line in file.readlines() if line.strip()]

file_names = read_file_names(file_list_path)

# Function to check if the file has been downloaded
def is_download_complete():
    downloaded_files = os.listdir(download_dir)
    for file_name in file_names:
        for downloaded_file in downloaded_files:
            if file_name in downloaded_file:
                return True
    return False

# Initialize counters for processed and remaining files
total_files = len(file_names)
processed_files = 0

# Iterate through the file names and try to download each
for file_name in file_names:
    print(f"Trying to download: {file_name}")
    
    # Find the input field by ID and enter the file name
    try:
        input_field = driver.find_element(By.ID, "filename")  # Replace with the actual ID
        input_field.clear()
        input_field.send_keys(file_name)  # Enter the file name
        
        # Find and click the button by ID
        button = driver.find_element(By.XPATH, "/html/body/div/form/button")
        button.click()
        
        # Wait for download to complete or timeout
        start_time = time.time()
        while time.time() - start_time < 15:  # Wait for a maximum of 15 seconds (adjust as needed)
            if is_download_complete():
                print(f"Download completed for {file_name}")
                break
            time.sleep(1)  # Sleep 1 second before checking again
        
        if not is_download_complete():
            print(f"No download detected for {file_name}. Checking if it redirected to /download.")
            # Check if it redirected to /download
            if "/download" in driver.current_url:
                print("Redirected to /download, returning to main page.")
                driver.get("https://lakshyactf-web2.onrender.com/")  # Go back to the main page
                time.sleep(0.5)  # Give time for the page to load

    except Exception as e:
        print(f"Error occurred while processing {file_name}: {e}")
    
    # Update the progress and display it
    processed_files += 1
    remaining_files = total_files - processed_files
    print(f"Processed {processed_files}/{total_files} files. {remaining_files} files left.")
    
    # Proceed to the next file, even if the current download wasn't successful
    print(f"Finished attempting download for {file_name}. Moving to next file...")

# Close the driver after completing all downloads
driver.quit()
