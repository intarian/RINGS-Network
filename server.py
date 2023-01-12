#%% This is just a demo presentation of a client server communication. The client sends the numpy array to server;
# The server scales the array by 2 and sends the information back to client.

import socket
import numpy as np

import json
from json import JSONEncoder


HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)


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
                ## Receive data from client
                data_r = data.decode("utf-8")
                data_json = json.loads(data_r)
                decodedArrays = np.asarray(data_json["array"])
                ## Start Computation or run algorithm on numpy matrix
                print('Received Matrix at Server: ')
                print(decodedArrays)
                data = decodedArrays@decodedArrays
                ## Convert back to json
                numpyData = {"array": data}
                data_s_json = json.dumps(numpyData, cls=NumpyArrayEncoder)
                data_s_bytes = bytes(data_s_json,encoding="utf-8")
                conn.sendall(data_s_bytes)