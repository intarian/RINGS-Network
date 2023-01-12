import socket
import numpy as np

import json
from json import JSONEncoder

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)

numpyArrayOne = np.array([[11, 22, 33], [44, 55, 66], [77, 88, 99]])

# Serialization
numpyData = {"array": numpyArrayOne}
encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)  # use dump() to write array into file


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(bytes(encodedNumpyData,encoding="utf-8"))
    data = s.recv(1024)

## Print received data from json to numpy
data_r = data.decode("utf-8")
data_json = json.loads(data_r)
decodedArrays = np.asarray(data_json["array"])
print('Received Matrix from Server: ')
print(decodedArrays)