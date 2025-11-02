import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load Excel data
file_path = 'secret_1_.xlsx'
df = pd.read_excel(file_path, usecols=[0], engine='openpyxl')
coordinates = df.iloc[1:, 0].dropna().tolist()

# Parse coordinates
coords = []
max_row = max_col = 0

for entry in coordinates:
    try:
        row, col = map(int, str(entry).split(','))
        coords.append((row, col))
        max_row = max(max_row, row)
        max_col = max(max_col, col)
    except Exception as e:
        print(f"Skipping invalid entry '{entry}': {e}")

# Create an empty grid (all white = 0)
grid = np.zeros((max_row + 1, max_col + 1), dtype=int)

# Fill black pixels (1s) at the specified coordinates
for row, col in coords:
    grid[row, col] = 1

# Plot it like a QR code
plt.figure(figsize=(8, 8))
plt.imshow(grid, cmap='binary', interpolation='none')  # black & white, no smoothing
plt.axis('off')
plt.title("QR-style Grid from Coordinates")
plt.tight_layout()
plt.show()
