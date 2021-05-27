import sys
import socket
import string
import random

ip_address = ['192.168.122.175', '192.168.122.197']

for ip in ip_address:
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = (ip, 10000)
    print(f"connecting to {server_address}")
    sock.connect(server_address)

    try:
        # Send data
        # If want to send 2 megabytes string data, change 64 to 2097152
        # 2 megabytes = 2097152 bytes
        message = ''.join(random.choice(string.ascii_letters) for i in range(64))
        print(f"sending {message}")
        sock.sendall(message.encode())

        # Look for the response
        amount_received = 0
        amount_expected = len(message)
        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            print(f"{data}")
    finally:
        print("closing")
        sock.close()
