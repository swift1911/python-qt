import os
import sys
import time
import thread
import sqlite3
import socket
from socket import *
import struct
from PyQt4.QtGui import *  
from PyQt4.QtCore import *
from PyQt4 import QtGui
from PyQt4.QtSql import *
from SocketServer import TCPServer, BaseRequestHandler  
import traceback 
from fileinput import filename

#global var
ip=gethostbyname(gethostname())
recvSock = socket(AF_INET,SOCK_STREAM)
BUFSIZE = 1024
data =""
FILEINFO_SIZE=struct.calcsize('128s32sI8s')
orw=None
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
        dataaction.triggered.connect(self.qsearch)
        dataaction.setStatusTip('manage order on server')
        startaction=QtGui.QAction(QtGui.QIcon('start.png'), '&start service', self) 
        startaction.triggered.connect(self.sbuttonclicked)
        startaction.setStatusTip('start service')
        stopaction=QtGui.QAction(QtGui.QIcon('stop.png'), '&stop service', self) 
        stopaction.triggered.connect(self.pbuttonclicked)
        stopaction.setStatusTip('stop service')
        managepiece=QtGui.QAction(QtGui.QIcon('piece.png'),'&manage piece',self)
        managepiece.triggered.connect(self.databasemanage)
        
        self.statusBar()
        menubar = self.menuBar()
        
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)
        datamenu=menubar.addMenu('&data')
        datamenu.addAction(dataaction)
        datamenu.addAction(managepiece)
        servicemenu=menubar.addMenu('&service')
        servicemenu.addAction(startaction)
        servicemenu.addAction(stopaction)        
        self.setWindowTitle('canteen order server')
        self.statusBar().showMessage('Ready')
        self.resize(640,480)
        self.move(320,160)        
        self.show()
    def databasemanage(self):
        loaddata(self)
    def qpiece(self):
        table2=PieceDialog()
        table2.exec_()
    def qsearch(self):
        loadorder(self)
    def sbuttonclicked(self):
        self.start(fileserver,1,8000)
        self.start(dataserver,1,7000)
    def pbuttonclicked(self):
        thread.exit_thread()
    def start(self,sname,arg1,arg2):
        thread.start_new_thread(sname,(arg1,arg2)) 
class MyDialog(QDialog):  
    def __init__(self, parent=None):  
        super(MyDialog, self).__init__(parent)  
        self.resize(640,480)
        self.setWindowTitle("order management")
        self.MyTable = QTableWidget(4,3)  
        self.MyTable.setHorizontalHeaderLabels(['table','picec','waitter'])  
        
        newItem = QTableWidgetItem("1")  
        self.MyTable.setItem(0, 0, newItem)  

        newItem = QTableWidgetItem("humberger")  
        self.MyTable.setItem(0, 1, newItem)  

        newItem = QTableWidgetItem("dyl")  
        self.MyTable.setItem(0, 2, newItem)   

        
        layout = QHBoxLayout()  
        layout.addWidget(self.MyTable)  
        self.setLayout(layout) 
        
        
        def updateProgress(self, value):
            newLine=QTableWidgetItem("2")
            self.MyTable.setItem(1,0,newLine)
        updateProgress(self, 0)
def createConnection(self): 
    db=QSqlDatabase.addDatabase("QSQLITE") 
    db.setDatabaseName("new_sq.db") 
    db.open() 

class Model2(QSqlTableModel):
    def __init__(self,parent): 
        QSqlTableModel.__init__(self,parent) 
        self.setTable("orderlist") 
        self.select() 
        self.setEditStrategy(QSqlTableModel.OnManualSubmit)
        
class Model(QSqlTableModel): 
    def __init__(self,parent): 
        QSqlTableModel.__init__(self,parent) 
        self.setTable("name") 
        self.select() 
        self.setEditStrategy(QSqlTableModel.OnManualSubmit)
        
            
class ormanage(QDialog):
    def __init__(self): 
        QDialog.__init__(self) 
        vbox=QVBoxLayout(self) 
        self.setWindowTitle("order management")
        self.view=QTableView() 
        self.model=Model2(self.view)
        
        self.resize(640,480)
        self.view.setModel(self.model) 
        vbox.addWidget(self.view)
    def updateui(self):
        QDialog.__init__(self) 
        vbox=QVBoxLayout(self) 
        self.setWindowTitle("order management")
        self.view=QTableView() 
        self.model=Model2(self.view)
        
        self.resize(640,480)
        self.view.setModel(self.model) 
        vbox.addWidget(self.view) 
class TestWidget(QDialog): 
    def __init__(self): 
        QDialog.__init__(self) 
        vbox=QVBoxLayout(self) 
        self.view=QTableView() 
        self.model=Model(self.view) 
        #self.changeEvent(Model2.submit())
        self.resize(640,480)
        self.view.setModel(self.model) 
        vbox.addWidget(self.view) 
        
class PieceDialog(QDialog):  
    def __init__(self, parent=None):  
        super(PieceDialog, self).__init__(parent)  
        self.resize(640,480)
        self.setWindowTitle("manage piece")
        self.MyTable = QTableWidget(50,2)
        self.MyTable.setHorizontalHeaderLabels(['name','price'])
        
        layout = QHBoxLayout()  
        layout.addWidget(self.MyTable)  
        self.setLayout(layout) 
def loaddata(self):
    createConnection(self)
    w=TestWidget()
    w.exec_()   
def loadorder(self):
    createConnection(self)
    orw=ormanage()
    orw.exec_()    
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
            global data
            data = self.request.recv(1024).strip()
            print "receive from (%r):%r" % (self.client_address, data) 
            #data.sub("0x00", "", str)
            #print struct.pack("x",*data)
            data=data.replace("\x00","")
            print data
            source=data.split(",")
            table=source[len(source)-2]
            waitter=source[len(source)-1]
            order=""
            for i in range(0,len(source)-2):
                order+=source[i]
            sconn=sqlite3.connect("new_sq.db")
            sconn.text_factory = sqlite3.OptimizedUnicode
            su=sconn.cursor()
            
            su.execute("insert into orderlist(tableno,piece,waitter) values('"+table+"','"+order+"','"+waitter+"');")
            sconn.commit()
            
            sconn.close()
            #self.request.sendall("\x00")
            loadorder(self)
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
    #filename='new_sq.db'
    #fhead=struct.pack('128s11I',filename,0,0,0,0,0,0,0,0,os.stat(filename).st_size,0,0)
    #conn.send(fhead)
    dirr=os.getcwd()
    l=os.listdir(dirr)
    for filename in l:
        if filename!=sys.argv[0][sys.argv[0].rfind(os.sep)+1:]:
            print filename
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
