#!/usr/bin/python3

import socket
print("test")

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()

port = 444

# connecting the port
clientsocket.connect((host,port))

message = clientsocket.recv(1024)

clientsocket.close()

print(message.decode('ascii'))

