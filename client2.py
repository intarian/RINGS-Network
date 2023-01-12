import socket
import numpy as np
from functions import *

ClientMultiSocket = socket.socket()
host = '127.0.0.1'
port = 2004
# print('Waiting for connection response')

try:
    ClientMultiSocket.connect((host, port))
except socket.error as e:
    print(str(e))
res = ClientMultiSocket.recv(1024)

## Send the data to server
while True:
    numpyArrayOne = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    data_enc = data_encoder(numpyArrayOne)
    ClientMultiSocket.send(data_enc)
    # Received Processed Data
    res = ClientMultiSocket.recv(1024)
    data_r_dec = data_decoder(res)
    print(data_r_dec)
    # Close connection after showing the data
    clos_cnnc = str(input('Should I close the connection (Y/N): '))
    if (clos_cnnc == 'Y'):
        print('Connection is closed')
        ClientMultiSocket.close()
        break

