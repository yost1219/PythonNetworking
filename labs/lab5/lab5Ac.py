"""
Author: Yost
Title: Lab 5A - client
Date: 27 Sep 2018

Lab 5A:

Write a TCP Server that will generate a random number from 0 to 100. Then write a TCP Client that
will receive an input from the user (number 0 to 100) and send the guess to the server. The server
will then send back a message prompting the user to guess higher or lower. If the user guesses the
correct number, have the server send back a success message and when the client receives the
success message it will break the connection (close the socket).
"""
from socket import *
​
#define function for input validation
def guess():
    input = raw_input("Input your guess.")
    try:
        input = int(input)
    except: ValueError:
        print "Not a valid guess."
        input = guess()
    return input
#setup client
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("localhost",15000))

#loop
while True:
#get question from server​
    message = s.recv(1024)
    print message
#answer server
    answer = guess()
    s.send(answer)
#get response from server
    response = s.recv(1024)
    print response
    
#close client
s.close()