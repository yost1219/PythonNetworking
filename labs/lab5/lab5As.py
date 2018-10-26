"""
Author: Yost
Title: Lab 5A - server
Date: 27 Sep 2018

Lab 5A:

Write a TCP Server that will generate a random number from 0 to 100. Then write a TCP Client that
will receive an input from the user (number 0 to 100) and send the guess to the server. The server
will then send back a message prompting the user to guess higher or lower. If the user guesses the
correct number, have the server send back a success message and when the client receives the
success message it will break the connection (close the socket).
"""
from socket import *

#setup server
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("",15000)) 
s.listen(5)
c,a = s.accept()

#generate random number
rand = random.randint(0,100)

#start loop
while True:
#ask client question
    question = "Guess what the random number is between 0 and 100."
    s.send(question)
#​get guess from client
    guess = c.recv(1024)
#check guess to see if it needs to be higher, lower, or if they got it right
#if higher tell them so, if lower tell them so, if right tell them so and close connection 
    if guess == rand:
        message = "YOU DID IT!  Dudu dudu dudu dudu duuuduuu!"
        s.send(message)
#close server
        s.close()
    elif guess < rand:
        message = "Your guess was too low.  Guess again, chump."
        s.send(message)
    else:
        message = "Your guess was too high.  What are you even doing?"
        s.send(message)
		
#close server
s.close()