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

#ask for user input of domain/url
domainName = raw_input("Enter a domain name: ")

#get ip address
ipAddress = gethostbyname(domainName)
domain = gethostbyaddr(ipAddress)exit

#print IP address
print "Domain's name is: {}".format(ipAddress[0])
print "Domain's IP address is: {}".format(ipAddress[2])