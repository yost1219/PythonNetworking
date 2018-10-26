"""
Author: Yost
Title: Networking Lab 1B-server
Date: 19 Sep 2018
"""
#setup server
from socket import *
s = socket(AF_INET6,SOCK_STREAM)
s.bind(("",15000))
s.listen(5) 
c,a = s.accept()

#go setup client
message = c.recv(1024)
print message #prints "Whazzap!!!"

#respond to client
c.send("Wasabi!")

#close connection
c.close()
