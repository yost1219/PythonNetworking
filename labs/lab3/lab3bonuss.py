"""
Author: Yost
Title: Lab 3 Bonus
Date: 25 Sep 2018

Bonus:  
Create a port scanner. Code it in Python, C, or Raw Sockets. Use IPv4 or IPv6, TCP and/or UDP.
"""
from socket import *

#setup server
s = socket(AF_INET,SOCK_STREAM)
s.bind(("",15000))
s.listen(5)
c,a = s.accept()

#ask question
question = "What site would you like to scan?"
c.send(question)

#get answer
answer = c.recv(1024)

#connect to target
targetIP = gethostbyname(answer)

#scan ports
openPorts = set()
for port in range(1,1025):
    s2 = socket(AF_INET,SOCK_STREAM)
    result = s2.connect_ex((targetIP,port))
#store open ports as list
    if result == 0:
        openPorts.add(port)

#close connection to target
s2.close()

#send response
s.send(openPorts)

#close server
s.close()