import pickle
import codecs
import os
import sys

def load_rpa(file):
    key = int(file[25:33], 16)
    index = pickle.loads(codecs.decode(file[int(file[8:24], 16):], "zlib"))
    return {k: (offset ^ key, dlen ^ key, start) for k, v in index.items() for offset, dlen, start in v}

def process_rpa(file):
    for k, (offset, dlen, start) in load_rpa(file).items():
        os.makedirs("out/" + '/'.join(k.split("/")[0:-1]), exist_ok=True)
        with open("out/" + k, "wb") as f2:
            f2.write(file[offset:offset+dlen+1])

for i in sys.argv[1:]:
    with open(i, "rb") as x:
        process_rpa(x.read())
