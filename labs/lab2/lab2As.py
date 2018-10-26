"""
Author: Yost
Title: Lab 2-2A Server
Date: 21 Sep 2018

Lab 2A

Write a TCP server that receives a string, reverses order of the words, and sends it back to the client.

Write a TCP client to connect to print the response (build in IPv4).
"""
from socket import *

#setup server
s = socket(AF_INET,SOCK_STREAM)
s.bind(("",15000))
s.listen(5)
c,a = s.accept()
print c
print a
#receive string
string = c.recv(1024)

#reverse string order
string = string.split()
string.reverse()
response = " ".join(string)

#send it back
c.send(response)

#close
c.close()