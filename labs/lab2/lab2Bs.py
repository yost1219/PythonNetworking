"""
Author: Yost
Title: Lab 2-2B Server
Date: 21 Sep 2018

Write a UDP sender that takes a dictionary, turns it into a JSON string, and sends it to a listener.

Write the UDP receiver to receive the JSON string and turns it back into a dictionary.

Validate by printing the type of your dictionary variable (build in IPv4).
"""
from socket import *
import json

#setup server/receiver
s = socket(AF_INET,SOCK_DGRAM)
s.bind(("",15000))

#receive JSON string
jsonStr, addr = s.recvfrom(1024)

#turn JSON back to dictionary
myDict = json.loads(jsonStr)

#print dictionary
print myDict

#close
s.close()
