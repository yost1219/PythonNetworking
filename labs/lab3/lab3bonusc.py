"""
Author: Yost
Title: Lab 3 Bonus
Date: 25 Sep 2018

Bonus:  
Create a port scanner. Code it in Python, C, or Raw Sockets. Use IPv4 or IPv6, TCP and/or UDP.
"""
from socket import *

#setup client
s = socket(AF_INET,SOCK_STREAM)
s.connect(("localhost",15000)) #localhost is 192.168.202.154

#receive question
question = s.recv(1024)

#send answer
answer = "www.google.com"
s.send(answer)

#get and print response
openPorts = s.recv(1024)
for port in openPorts:
    print "Port {} is open.".format(port)

#close client
s.close()