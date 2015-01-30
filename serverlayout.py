import os
import sys
import time
import thread
from socket import *
import struct
from PyQt4 import QtGui
from SocketServer import TCPServer, BaseRequestHandler  
import traceback 

#global var
ip="192.168.1.105"

#end

class qmain(QtGui.QMainWindow):
    def __init__(self):
        super(qmain, self).__init__()
        self.initui()
        #self.start()
    def initui(self):
        sbutton=QtGui.QPushButton("打开文件服务器",self)
        sbutton.show()
        sbutton.resize(150,50)
        pbutton=QtGui.QPushButton("关闭文件服务器",self)
        pbutton.show()
        pbutton.resize(150,50)        
        pbutton.move(170,0)
        sbutton.clicked.connect(self.sbuttonclicked)
        self.resize(640,480)
        self.move(320,160)
        self.show()
    def sbuttonclicked(self):
        self.start(fileserver,1,8000)
    def start(self,sname,arg1,arg2):
        thread.start_new_thread(sname,(arg1,arg2))  
        #thread.start_new_thread(dataserver,(1,7000))
class MyBaseRequestHandlerr(BaseRequestHandler):   
    def handle(self):   
        while True:  
            try:  
                data = self.request.recv(1024).strip()  
                print "receive from (%r):%r" % (self.client_address, data)  
                #self.request.sendall("\x00")
                self.request.sendall(data.upper())  
            except:  
                traceback.print_exc()  
                break
def dataserver(arg1,arg2):    
    global ip  
    #port = 8000    
    address = (ip, arg2)   
    server = TCPServer(address, MyBaseRequestHandlerr)  
    server.serve_forever()
def fileserver(arg1,arg2):
    global ip
    ADDR = (ip,arg2)
    BUFSIZE = 1024
    FILEINFO_SIZE=struct.calcsize('128s32sI8s')
    recvSock = socket(AF_INET,SOCK_STREAM)
    recvSock.bind(ADDR)
    recvSock.listen(True)
    print "waiting for conncetion..."
    conn,addr = recvSock.accept()
    print "client has connceted to > ",addr
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
def main():
    app = QtGui.QApplication(sys.argv)
    ex = qmain()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()


