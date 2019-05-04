import pickle
import os
import sys
import struct
import zlib

RPYC2_HEADER = "RENPY RPC2"
def read_script(r):
    header_data = r[:1024]
    pos = len(RPYC2_HEADER)

    o = bytes()
    while pos + 12 < len(header_data):
        header_slot, start, length = struct.unpack("III", header_data[pos:pos+12])
        if header_slot == 0:
            break
        pos += 12
        o += zlib.decompress(r[start:start+length])

        # TODO(ym):
        # o += pickle.loads(zlib.decompress(f.read(length)))
    return o

os.makedirs("out_script", exists_ok=True)
for i in sys.argv[1:]:
    o = open("out_script/" + i.split('/')[-1], "wb")
    o.write(read_script(open(i, "rb").read()))
    o.close()
