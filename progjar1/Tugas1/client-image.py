import sys
import socket

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
        send_image = 'send_image.jpeg'
        recv_image = 'recv_image-alpine-' + str(ip_address.index(ip)) + '.jpeg'

        filename = open(send_image, 'rb')
        image = filename.read()

        print(f"sending {send_image}")
        sock.sendall(image)

        # Look for the response
        amount_received = 0
        amount_expected = len(image)
        with sock, open(recv_image, 'wb') as img:
            while amount_received < amount_expected:
                data = sock.recv(16)
                amount_received += len(data)
                if not data: break
                img.write(data)
    finally:
        print(f"receiving {recv_image}")
        print("closing")
        sock.close()