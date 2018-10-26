"""
Author: Yost
Title: Lab 4A server
Date: 26 Sep 2018

Create a simple TCP chat server that connects to multiple clients using IPv4 and either Select()
or Threading. Then echo back data to all clients using broadcasts (Use multiple VM's and track
traffic in Wireshark).
"""
from socket import *
import select

#setup server and client connections
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s1.setblocking(0)
s1.bind(("",2000))
s1.listen(1)
s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2.setblocking(0)
s2.bind(("",s2port))
s2.listen(1)

#sockets to read
inputs = [s1,s2]

#sockets to write
outputs = []


#receive messages and broadcast items

#close server after all clients close their connections