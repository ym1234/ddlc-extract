import pickle
import os
import sys
import struct
import zlib

RPYC2_HEADER = "RENPY RPC2"
def read_script(r):
    header_data = r[:1024]

    o = bytes()
    for pos in range(len(RPYC2_HEADER), len(header_data), 12):
        header_slot, start, length = struct.unpack("III", header_data[pos:pos+12])
        if header_slot == 0:
            break
        o += zlib.decompress(r[start:start+length])

        # TODO(ym): acutally load the class files and extract the dialouge out of them/process them somehow
        # pickle.loads(zlib.decompress(f.read(length)))
    return o

os.makedirs("out_script", exist_ok=True)
for i in sys.argv[1:]:
    with open(f"out_script/{i.split('/')[-1] + '.out'}", "wb") as o, open(i, "rb") as x:
        o.write(read_script(x.read()))
