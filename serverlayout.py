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
recvSock = socket(AF_INET,SOCK_STREAM)
BUFSIZE = 1024
FILEINFO_SIZE=struct.calcsize('128s32sI8s')
#end

class qmain(QtGui.QMainWindow):
    def __init__(self):
        super(qmain, self).__init__()
        self.initui()
        #self.start()
    def initui(self):
        exitAction = QtGui.QAction(QtGui.QIcon('stop.png'), '&Exit', self)        
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(QtGui.qApp.quit)
        dataaction=QtGui.QAction(QtGui.QIcon('database.png'),'&manage order',self)
        dataaction.triggered.connect(qsearch)
        dataaction.setStatusTip('manage order on server')
        startaction=QtGui.QAction(QtGui.QIcon('start.png'), '&start service', self) 
        startaction.triggered.connect(self.sbuttonclicked)
        startaction.setStatusTip('start service')
        stopaction=QtGui.QAction(QtGui.QIcon('stop.png'), '&stop service', self) 
        stopaction.triggered.connect(self.pbuttonclicked)
        stopaction.setStatusTip('stop service')
        self.statusBar()
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)
        datamenu=menubar.addMenu('&data')
        datamenu.addAction(dataaction)
        servicemenu=menubar.addMenu('&service')
        servicemenu.addAction(startaction)
        servicemenu.addAction(stopaction)        
        self.setWindowTitle('canteen order server')
        self.statusBar().showMessage('Ready')
        self.resize(640,480)
        self.move(320,160)        
        self.show()
    def sbuttonclicked(self):
        self.start(fileserver,1,8000)
        self.start(dataserver,1,7000)
    def pbuttonclicked(self):
        thread.exit_thread()
    def start(self,sname,arg1,arg2):
        thread.start_new_thread(sname,(arg1,arg2)) 
class qsearch(QtGui.QMainWindow):
    def __init__(self):
        super(qsearch,self).__init__()
        self.initui()
    def initui(self):
        self.resize(640,480)
        self.move(320,160)
        self.show()
class MyBaseRequestHandlerr(BaseRequestHandler):   
    def handle(self):     
        try:  
            data = self.request.recv(1024).strip()
            print "receive from (%r):%r" % (self.client_address, data) 
            #data.sub("0x00", "", str)
            print data
            #self.request.sendall("\x00")
            self.request.sendall(data.upper())  
        except:  
            traceback.print_exc()  
def dataserver(arg1,arg2):    
    global ip  
    #port = 8000    
    address = (ip, arg2)   
    server = TCPServer(address, MyBaseRequestHandlerr)  
    server.serve_forever()
def fileserver(arg1,arg2):
    global ip
    global recvSock
    ADDR = (ip,arg2)
    if arg1==1:
        recvSock.bind(ADDR)
        recvSock.listen(True)
    print "waiting for conncetion..."
    transport(recvSock.accept())
def transport(arg1):
    global BUFSIZE
    global recvSock
    if arg1==None:
        return 
    conn,addr = arg1
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
    #recvSock.close()
    conn.close()
    print "conncetion has been closed"
    fileserver(2,8000)
def main():
    app = QtGui.QApplication(sys.argv)
    ex = qmain()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()


