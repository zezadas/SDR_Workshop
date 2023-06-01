#!/bin/python3
# python3 -u decode_bin_slicer.py

import os,sys
from pathlib import Path
circ_size=30
circ_index=0
circ_array=[b"\x00"]*circ_size

path = "/tmp/comando.fifo"
fifo_path = Path(path)
#recreate fifo file
if (not fifo_path.is_fifo()):
    os.remove(path)
    os.mkfifo(fifo_path)
waiting = True
#open fifo and read 1 byte
with fifo_path.open("rb") as f:
    while True:
       
        byte=f.read(1)

        circ_array[circ_index%circ_size]=byte
        circ_index += 1
        if (circ_index%circ_size==0):
            circ_index=0
        if(circ_array==[b"\x00"]*circ_size):
            waiting = True
            continue
        if (waiting==True):
            waiting = False
            print("\n")

        bval="X"
        if (byte==b"\x00"):
            bval = "0"
        elif(byte==b"\x01"):
            bval = "1"
        else:
            pass
        print(bval,end="")

