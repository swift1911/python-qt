# -*- coding: cp936 -*-
import os
import time
from socket import *
import struct
ADDR = ('192.168.1.105',8000)
BUFSIZE = 1024
FILEINFO_SIZE=struct.calcsize('128s32sI8s')
recvSock = socket(AF_INET,SOCK_STREAM)
recvSock.bind(ADDR)
recvSock.listen(True)
print "waiting for conncetion..."
conn,addr = recvSock.accept()
print "client has connceted—> ",addr
#sendSock = socket(AF_INET,SOCK_STREAM)
#sendSock.connect(ADDR)
filename='new_sq.db'
fhead=struct.pack('128s11I',filename,0,0,0,0,0,0,0,0,os.stat(filename).st_size,0,0)

conn.send(fhead)

fp = open(filename,'rb')
while 1:
    filedata = fp.read(BUFSIZE)
    if not filedata: 
        break
    conn.send(filedata)
print "transfer finished,drop conncetion"
fp.close()
recvSock.close()
conn.close()
print "conncetion has been closed"


