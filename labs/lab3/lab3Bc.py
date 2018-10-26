"""
Author: Yost
Title: Lab 3B - Client
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

#setup client
s = socket(AF_INET,SOCK_DGRAM)

#initialize a string
string1 = "This is the original string"

#send the string
s.sendto(string1,("localhost",15000)) #localhost is 192.168.202.154

#receive and print the new string
string2, addr = s.recvfrom(1024)
print string2

#close client
s.close()