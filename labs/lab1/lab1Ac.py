"""
Author: Yost
Title: Networking Lab 1A-client
Date: 19 Sep 2018
"""
#after server is setup
from socket import *
s = socket(AF_INET,SOCK_STREAM)
s.connect(("localhost",15000)) #localhost is 192.168.202.154

#send message
s.send("Whazzap!!!")

#get response
response = s.recv(1024)
print response #prints "Wasabi!"

#close connection
s.close()

