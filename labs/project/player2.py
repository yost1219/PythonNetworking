"""
Team: BWPY
Title: Player 1
Date: 1 Oct 2018

"""
from socket import *
import struct

host = '127.0.0.1' #for single machine, address is '192.168.202.159' on linux vm

#setup player cxn
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,5002))