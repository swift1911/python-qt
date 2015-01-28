# -*- coding: cp936 -*-

from socket import *
import struct
ADDR = ('192.168.1.105',8000)
BUFSIZE = 1024
FILEINFO_SIZE=struct.calcsize('128s32sI8s')
conn = socket(AF_INET,SOCK_STREAM)
#socket.setdefaulttimeout(1000)
conn.connect(ADDR)
conn.send("\x00\x00")

fhead = conn.recv(FILEINFO_SIZE)
filename,temp1,filesize,temp2=struct.unpack('128s32sI8s',fhead)
print filename,len(filename),type(filename)
print filesize
filename = filename.strip('\00') #...
fp = open(filename,'wb')
restsize = filesize
print "正在接收文件... ",
while 1:
    if restsize > BUFSIZE:
        filedata = conn.recv(BUFSIZE)
    else:
        filedata = conn.recv(restsize)
    if not filedata: break
    fp.write(filedata)
    restsize = restsize-len(filedata)
    if restsize == 0:
        break
print "接收文件完毕，正在断开连接..."
fp.close()
conn.close()
print "连接已关闭..."
