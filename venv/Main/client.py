import socket
import sys

IP = '127.0.0.1'
PORT = 1234
HEADERSIZE = 15

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))

client_socket.setblocking(False)

username = input("Enter Username: ")
en_username = username.encode('utf-8')
client_socket.send((f"{len(en_username):<{HEADERSIZE}}"+username).encode('utf-8'))
protocol = input("Enter the protocol (S or L): ")
en_protocol = protocol.encode('utf-8')
client_socket.send((f"{len(en_protocol):<{HEADERSIZE}}"+protocol).encode('utf-8'))

while True:
    try:
        while True:
            message_header = client_socket.recv(HEADERSIZE)
            message_size = int(message_header.decode('utf-8'))
            message = client_socket.recv(message_size).decode('utf-8')
            client_socket.setblocking(False)
            print(f"The server said: {message}")
    except:
        pass

    client_message = input("Say something: ")
    if client_message == 'Quit':
        sys.exit()
    encoded_message = client_message.encode('utf-8')
    client_socket.send((f"{len(encoded_message):<{HEADERSIZE}}"+client_message).encode('utf-8'))
    client_socket.setblocking(True)
