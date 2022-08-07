#!/usr/bin/env python

import sys, binascii

key = sys.argv[2]
mode = sys.argv[3]
keyidx = 0
xored = ''

if mode == 'enc':
    msg = sys.argv[1]
elif mode == 'dec':
    msg = binascii.unhexlify(sys.argv[1])

for msgchar in msg:
    xored += chr(ord(key[keyidx%len(key)]) ^ ord(msgchar))
    keyidx += 1

if mode == 'enc':
    print (binascii.hexlify(xored))    
elif mode == 'dec':
    print (xored) 