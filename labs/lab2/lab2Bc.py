"""
Author: Yost
Title: Lab 2-2B Client
Date: 21 Sep 2018

Write a UDP sender that takes a dictionary, turns it into a JSON string, and sends it to a listener.

Write the UDP receiver to receive the JSON string and turns it back into a dictionary.

Validate by printing the type of your dictionary variable (build in IPv4).
"""
from socket import *
import json

#setup client/sender
s = socket(AF_INET,SOCK_DGRAM)

#take a dictionary, turn it into JSON string
myDict = {'name':'John', 'position':'QB', 'number':7}
jsonStr = json.dumps(myDict)

#send JSON to listener
s.sendto(jsonStr,("localhost",15000)) #localhost is 192.168.202.154

#close
s.close()
