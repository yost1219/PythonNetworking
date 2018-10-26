"""
Author: Yost
Title: Lab 2-2C Client
Date: 21 Sep 2018

Write a simple socket program that will send back your machine's Host name and IP Address.

(Don't forget to use your resources (Pydocs, Man pages). You can also get formatting help from the
python interpreter by using help(socket.gethostname) and help(socket.gethostbyname) after importing
the socket library.)
"""
from socket import *

#setup client
s = socket(AF_INET,SOCK_STREAM)
s.connect(("localhost",15000)) #localhost is 192.168.202.154

#pull own machine's host name and IP address
hostName = gethostname()
ipAddress = gethostbyname(hostName)

#send that info to server
s.send(hostName)
s.send(ipAddress)

#close
s.close()