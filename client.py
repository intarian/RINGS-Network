import socket
import numpy as np

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server
# integer_val = 2000
# bytes_val = integer_val.to_bytes(5, 'big')
x = np.array([[0, 1.6], [2, 3]], dtype='float64')
ba = x.tobytes()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(ba)
    data = s.recv(1024)
print('Received Data: ')
print(np.frombuffer(data,dtype='float64'))