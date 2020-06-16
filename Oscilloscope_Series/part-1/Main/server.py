import socket
from cmd_parser import *
import sys

HEADERSIZE = 15
IP = '127.0.0.1'
PORT = 1234

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((IP, PORT))
server_socket.listen(0)

clientSocket = None
addr = None

username = None
protocol = None

#Initializing state machines
Initialize_stateM()

def recieve_message():
    try:
        message_header = clientSocket.recv(HEADERSIZE)

        if not len(message_header):
            return False

        message_length = int(message_header.decode('utf-8'))
        return {"Header":message_header, "data":clientSocket.recv(message_length)}
    except:
        return False

def commands(cmd):

    if protocol.upper() == 'L':
        response = parse_long(cmd)
    else:
        response = parse_short(cmd)
    
    return response 

while True:
        if clientSocket is None:
            clientSocket, addr = server_socket.accept()
            print(f"{addr} is now connected")
            #clientSocket.send(("Welcome to the dark side").encode('utf-8'))
        try:
            if username is None:
                header = clientSocket.recv(HEADERSIZE)
                message_len = int(header.decode('utf-8'))
                username = clientSocket.recv(message_len).decode('utf-8')
                header = clientSocket.recv(HEADERSIZE)
                message_len = int(header.decode('utf-8'))
                protocol = clientSocket.recv(message_len).decode('utf-8')
                
            message = recieve_message()

        except:
            message = ''

        decMsg = message['data'].decode('utf-8')
        if decMsg.upper() == 'QUIT SERVER':
            print("Quiting the server.. .brace yourself")
            sys.exit()

        if not len(message['data']):
            print(f"{addr} is no longer connected")
            clientSocket = None
            addr = None
            username = None
            protocol = None
        else:
            print(f"{username}: {message['data'].decode('utf-8')}")
            response = commands(message['data'].decode('utf-8'))
            print(response)
            encodedMsg = response.encode('utf-8')
            clientSocket.send((f"{len(encodedMsg):<{HEADERSIZE}}"+response).encode('utf-8'))
