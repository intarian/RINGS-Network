#%% This is just a demo presentation of a client server communication. The client sends the numpy array to server;
# The server applies the algorithm and sends the information back to client.

import socket
import numpy as np
from functions import *
from _thread import *

ServerSideSocket = socket.socket()
host = '127.0.0.1'
port = 2004
ThreadCount = 0

try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))
print('Socket is listening..')
ServerSideSocket.listen(5)


def multi_threaded_client(connection):
    connection.send(str.encode('Server is working:'))
    while True:
        data = connection.recv(2048)
        response = 'Server message: ' + data.decode('utf-8')
        if not data:
            break
        else:
            data_dec = data_decoder(data)
            data_pr = run_algo(data_dec)
            data_pr_enc = data_encoder(data_pr)
        connection.sendall(data_pr_enc)
    connection.close()

while True:
    Client, address = ServerSideSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(multi_threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSideSocket.close()
