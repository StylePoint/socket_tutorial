#!/usr/bin/python3
# TSP SERVER

from http import client
from pydoc import cli
import socket
#socket.AF_INET = socket family socket.SOCK_STREAM= socket type
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#host = "ipv4"
# get the socket name
host = socket.gethostname()
# just port
port = 444

# binded host and port to socket
serversocket.bind((host, port))

# listens to connections in this case 3
serversocket.listen(3)
print("wtf")

while True:
    #Starting connection
    clientsocket,address = serversocket.accept()
    # Cliente connection request
    print("Recieved connection from %s"  % str(address))

    # Response to the client
    message = 'Thank you for connecting to the server' + "\r\n"
    # We need to encode message
    clientsocket.send(message.encode('ascii'))

    clientsocket.close()