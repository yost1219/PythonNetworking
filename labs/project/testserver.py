import socket

s = socket.socket()
s.bind(('',5000))
s.listen(4)
#wait for it
c,a = s.accept()
