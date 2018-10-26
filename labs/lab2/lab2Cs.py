"""
Author: Yost
Title: Lab 2-2C Server
Date: 21 Sep 2018

Write a simple socket program that will send back your machine's Host name and IP Address.

(Don't forget to use your resources (Pydocs, Man pages). You can also get formatting help from the
python interpreter by using help(socket.gethostname) and help(socket.gethostbyname) after importing
the socket library.)
"""
from socket import *

#setup server
s = socket(AF_INET,SOCK_STREAM)
s.bind(("",15000))
s.listen(5)
c,a = s.accept()

#receive information from client
hostName = c.recv(1024)
ipAddress = c.recv(1024)

#print client's host name and IP address
print "Client's host name is: {}".format(hostName)
print "Client's IP address is: {}".format(ipAddress)

#close
c.close()