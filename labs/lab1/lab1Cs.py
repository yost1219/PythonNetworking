"""
Author: Yost
Title: Networking Lab 1C-server
Date: 19 Sep 2018
"""
#setup server
from socket import *
s = socket(AF_INET,SOCK_DGRAM)
s.bind(("",15000))

#setup while
while True:
#get message from client
    message,address = s.recvfrom(1024)
    print message
    print address
#send response to client
    response = "Wasabi!"
    s.sendto(response,address)
