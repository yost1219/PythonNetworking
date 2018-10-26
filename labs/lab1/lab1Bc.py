"""
Author: Yost
Title: Networking Lab 1B-client
Date: 19 Sep 2018
"""
#after server is setup
from socket import *
s = socket(AF_INET6,SOCK_STREAM)
s.connect(("localhost",15000)) #local host is fe80::9f4f:704:e78b:cd5a

#send message
s.send("Whazzap!!!")

#get response
response = s.recv(1024)
print response #prints "Wasabi!"

#close connection
s.close()
