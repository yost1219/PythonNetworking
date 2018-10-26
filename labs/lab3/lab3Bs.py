"""
Author: Yost
Title: Lab 3B - Server
Date: 24 Sep 2018

Lab 3B

Write a UDP receiver that receives a string, and orders the words from longest to shortest in a
new string.

That new string should be sent to the remote port+1.

(i.e. the source port of message from the SENDER's POV)

Write a UDP sender that sends the initial string, and receives the response from the receiver
above (you can use multiple receivers or combine them).

Hint: The second step is intentionally ambiguous on how to proceed. There are multiple solutions.
"""
from socket import *

#setup server
s = socket(AF_INET,SOCK_DGRAM)
s.bind(("",15000))

#receive string
string1, addr = s.recvfrom(1024)

#reorder string from longest word to shortest word in new string
splitStr = string1.split()
#sortSplit = sorted(splitStr, key = len, reverse = True)
splitStr.sort(lambda x,y: cmp(len(y),len(s)))
string2 = " ".join(splitStr)

#send new string back
s.sendto(string2,("client",15000)) #client is 192.168.202.155

#close server
s.close()