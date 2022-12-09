#%% This is just a demo presentation of a client server communication. The client sends the numpy array to server;
# The server scales the array by 2 and sends the information back to client.

import socket
import numpy as np

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            else:
                print('Original Data received: ',np.frombuffer(data, dtype='float64'))
                data = np.frombuffer(data, dtype='float64')
                data = data*2
                data = data.tobytes()
                print('Data to be send back: ',np.frombuffer(data, dtype='float64'))
                conn.sendall(data)
