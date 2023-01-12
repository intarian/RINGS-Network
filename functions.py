import numpy as np
import json
from json import JSONEncoder


## Copied (I guess this encodes the numpy with json)
class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)

## Use to decode the stream to json and then to numpy array
def data_decoder(data): # input byte stream and output numpy arrays
    data_d = data.decode("utf-8")
    data_json = json.loads(data_d)
    decodedArrays = np.asarray(data_json["array"])
    return decodedArrays

## Use to encode the numpy to json and then to stream
def data_encoder(data): # input numpy arrays and output byte stream
    numpyData = {"array": data}
    data_s_json = json.dumps(numpyData,cls=NumpyArrayEncoder)
    data_s_bytes = bytes(data_s_json, encoding="utf-8")
    return data_s_bytes


## Run Algorithm
def run_algo(data): # input numpy arrays & output numpy array
    [ds, dv, dd] = np.linalg.svd(data)
    return ds
