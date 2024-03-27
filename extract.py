#!/bin/env python
import sys
f=open("BZ.MT7622_6.0.21+13673.220607.2004.bin", 'rb')
content=f.read()
header=content[:0x10C]
offset=0x10c
while offset < len(content):
    part=content[offset:offset+4]
    if(part.decode() != "PART"):
        print("ERROR detecting PART!")
        sys.exit(-1)
    part_name=content[offset+4:offset+4+0x2C]
    print("Detected partition: " + str(part_name))
    size=content[offset+0x30:offset+0x30+4]
    size_int=int.from_bytes(size)
    offset=offset+4+0x30+4
    payload=content[offset:offset+size_int+4]
    i = 0
    part_name_string = []
    while(part_name[i] != 0):
        i = i + 1
    part_name_string = part_name[0:i].decode()
    with open(part_name_string + ".bin", "bw") as out:
        out.write(payload)
    offset=offset+size_int+4+4

