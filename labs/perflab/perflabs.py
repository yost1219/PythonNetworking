"""
Author: Yost
Title: Performance Lab 4-2s
Date: 26 Sep 2018

Performance Lab:

Create a TCP client using IPv4. Pack the following values in a struct using network byte order:
12345, 56789, &, *, 0x7d0, 0b11111010000. Then send the packed struct to a TCP server and print
the unpacked values.
"""
from socket import *
import struct

#setup server
s = socket(AF_INET,SOCK_STREAM)
s.bind(("",15000))
s.listen(5)
c,a = s.accept()

#receive struct
data = c.recv(1024)

#unpack struct and put indexes 4 and 5 in correct format
structure = struct.unpack('!iiccii',data)
structure = set(structure)
structure[4] = hex(structure[4])
structure[5] = bin(structure[5])

#print struct
print structure

#close server
s.close()