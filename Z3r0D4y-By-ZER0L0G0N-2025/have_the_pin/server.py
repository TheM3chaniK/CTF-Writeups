import socket
import threading
import time

HOST = "0.0.0.0"
PORT = 5000  # Change to any open port
FLAG = "###REDACTED###"
PIN = "954312"  # 6-digit secret PIN

def handle_client(conn, addr):
    try:
        conn.sendall(b"Welcome to the challenge!\n")
        conn.sendall(b"Enter 6-digit PIN: ")

        data = conn.recv(1024).decode().strip()

        if not data:
            conn.close()
            return
        print("Checking...")
        time.sleep(5)
        if data == PIN:
            conn.sendall(f"Correct! Here is your flag:\n{FLAG}\n".encode())
        else:
            conn.sendall(b"Wrong PIN! Try again later.\n")

    except Exception as e:
        print(f"[!] Error handling {addr}: {e}")

    finally:
        conn.close()

def main():
    print(f"[*] Server listening on {HOST}:{PORT}")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(5)

    while True:
        conn, addr = server.accept()
        print(f"[+] Connection from {addr}")
        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.daemon = True
        client_thread.start()

if __name__ == "__main__":
    main()