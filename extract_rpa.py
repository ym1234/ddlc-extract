import pickle
import codecs
import os
import sys

def load_rpa(file):
    offset = int(file[8:24], 16)
    key = int(file[25:33], 16)
    index = pickle.loads(codecs.decode(file[offset:], "zlib"))

    # why is this xor encoded lmfao
    # TODO(ym): listcomp
    for (k, v) in index.items():
        # Isn't  needed for ddlc files
        # if len(v) == 2:
            # v = (v[0], v[1], '')
        index[k] = [(offset ^ key, dlen ^ key, start) for offset, dlen, start in v]

    return index

# TODO(ym): python probably has something to remove the need to create directory, open file, copy the content, close the file all manually.
def process_rpa(file):
    for (k, v) in load_rpa(file).items():
        os.makedirs("out/" + '/'.join(k.split("/")[0:-1]), exist_ok=True)
        f2 = open("out/" + k, "wb")

        offset, dlen, start = v[0]
        f2.write(file[offset:offset+dlen+1])
        f2.close()

for i in sys.argv[1:]: process_rpa(open(i, "rb").read())
