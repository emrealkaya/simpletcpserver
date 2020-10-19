#!/usr/bin/python

import socket

s = socket.socket()
host = socket.gethostname()
port = 4444
s.bind((host,port))

s.listen(10)
while True:
    c, addr = s.accept()
    print('connection from', addr)
    c.send("connecting")
    c.close()