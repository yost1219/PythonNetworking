"""
Author: Yost
Title: Performance Lab 4-2c
Date: 26 Sep 2018

Performance Lab:

Create a TCP client using IPv4. Pack the following values in a struct using network byte order:
12345, 56789, &, *, 0x7d0, 0b11111010000. Then send the packed struct to a TCP server and print
the unpacked values.
"""
from socket import *
import struct

#setup client
s = socket(AF_INET,SOCK_STREAM)
s.connect(("localhost",15000)) #localhost is 192.168.202.157

#create and pack struct
data = struct.pack('!iiccii',12345,56789,'&','*',0x7d0,0b11111010000)

#send struct
s.send(data)

#close client
s.close()