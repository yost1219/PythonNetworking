"""
Team: BWPY
Title: Server
Date: 1 Oct 2018

"""

from socket import *
import select
import sys
from thread import *
import struct


numPlayers= input()

s0=socket(AF_INET,SOCK_DGRAM)
s0.bind(('',5000))

sockets=[]
clients=[]


for x in range(1,numPlayers+1):
    ts = socket()
    sockets.append(ts)
    print ts
    print sockets[x-1]
    print x
    tc ,ta = s0.recvfrom(1024)
    while tc != "hello server":
        tc ,ta = s0.recvfrom(1024) 
    s0.sendto('{}'.format((5000+x)),ta)
    sockets[x-1].bind(('',5000+x))
    sockets[x-1].listen(1)
    print 'started listening'
    c,a = sockets[x-1].accept()
    clients.append(c)
#look/listen for connections on player ports
#players switch to assigned ports


#broadcast function
def sendAll(data):
	for c in clients:
		c.send(data)
    #c1.send(data)
    #c2.send(data)
    #c3.send(data)
    #c4.send(data)

#loop
while True:
#dump all data fields
    data1=''
    data2=''
    data3=''
    data4=''
#check for new data
    data1=c1.recv(1024)
    data2=c2.recv(1024)
    data3=c3.recv(1024)
    data4=c4.recv(1024)
#broadcast all received data if any
    if data1 != '':
        print "something at 1"
        sendAll(data1)
    if data2 != '':
        sendAll(data2)
    if data3 != '':
        sendAll(data3)
    if data4 != '':
        sendAll(data4)
		
#close sockets
s1.close()
s2.close()
s3.close()
s4.close()