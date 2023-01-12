import numpy as np
import json
from json import JSONEncoder



class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)


def data_decoder(data):
    data_d = data.decode("utf-8")
    data_json = json.loads(data_d)
    decodedArrays = np.asarray(data_json["array"])
    return decodedArrays

def run_algo(data): # assumes numpy arrays
    return data@data

def data_encoder(data):
    numpyData = {"array": data}
    data_s_json = json.dumps(numpyData,cls=NumpyArrayEncoder)
    data_s_bytes = bytes(data_s_json, encoding="utf-8")
    return data_s_bytes