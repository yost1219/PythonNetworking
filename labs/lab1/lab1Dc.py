"""
Author: Yost
Title: Networking Lab 1C-client
Date: 19 Sep 2018
"""
#after server is setup
from socket import *
s = socket(AF_INET6,SOCK_DGRAM)

#send message to server
message = "Whazzap!!!"
s.sendto(message,("localhost",15000)) #local host is fe80::9f4f:704:e78b:cd5a

#get response from server
response,address = s.recvfrom(1024)
print response
print address

