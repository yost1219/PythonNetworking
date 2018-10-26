"""
Author: Yost
Title: Lab 2-2A Client
Date: 21 Sep 2018

Lab 2A

Write a TCP server that receives a string, reverses order of the words, and sends it back to the client.

Write a TCP client to connect to print the response (build in IPv4).
"""
from socket import *

#setup client and connect to server
s = socket(AF_INET,SOCK_STREAM)
s.connect(("localhost",15000)) #localhost is 192.168.202.154

#send string
string = "This is my message to you"
s.send(string) 

#receive string
response = s.recv(1024)

#print items
print response

#close
s.close()