"""
Author: Yost
Title: Networking Lab 1C-client
Date: 19 Sep 2018
"""
#after server is setup
from socket import *
s = socket(AF_INET,SOCK_DGRAM)

#send message to server
message = "Whazzap!!!"
s.sendto(message,("localhost",15000)) #localhost is 192.168.202.154

#get response from server
response,address = s.recvfrom(1024)
print response
print address

