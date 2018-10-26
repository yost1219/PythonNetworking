"""
Author: Yost
Title: Lab 3A - Client
Date: 24 Sep 2018

Lab 3A

Using the struct package from the python library, pack the values (1, 2, -3, -4) as the following
data types (unsigned short, unsigned int, signed short, signed int)

1 as an unsigned short

2 as an unsigned int

-3 as a signed short

-4 as a signed int

Write a TCP client that packs those values, sends the packed string to a server.

Write a TCP server that receives the string, unpacks it using little endian and prints it, then
unpacks it again using big endian and prints it.
"""
from socket import *
import struct

#setup client
s = socket(AF_INET,SOCK_STREAM)
s.connect(("localhost",15000)) #localhost is 192.168.202.154

#pack data as struct
data = struct.pack('=HIhi',1,2,-3,-4)

#send data to server
s.send(data)

#close client
s.close()