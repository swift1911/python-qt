#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import socket
import binascii
import ssl
import sqlite3
import os
import struct
from socket import *
from PyQt4 import QtGui

#global varible

username=''
order=[]
spice=[]
meta=[]
tb=[]
index=0
page=0
maxpage=0
price=[]
address="172.21.199.2"
cport=7000
fport=8000
#end
class qmain(QtGui.QMainWindow):    
    def __init__(self):
        super(qmain, self).__init__()
        self.login()
        self.downloadsql()
        self.fetch_data(1)
        self.initUI(0)
    def initUI(self,p):  
        global index
        global page
        global tb
        for i in range(0,6):
            tb.append(i)
        index=0
        j=0
        last=len(meta)/6-page*6
        maxpage=len(meta)/6
        self.resize(320,240)
        self.move(0,0)
        self.setWindowTitle('canteen order system'+'username:'+username) 
        self.menuBar()
        try:
            index=page*6+j
	    tabhost=QtGui.QTabWidget(self)
	    tabhost.resize(320,240)
	    east=QtGui.QWidget()
	    west=QtGui.QWidget()
	    tabhost.addTab(east, "east")
	    tabhost.addTab(west,"west")
	    
            bt1=QtGui.QPushButton(meta[index]+" "+price[index],self)
            bt1.move(0,20)
            bt1.clicked.connect(self.buttonClicked1)
            bt1.show()
            j=j+1
            index=page*6+j
            bt2=QtGui.QPushButton(meta[index]+price[index],self)
            bt2.move(100,20)
            bt2.clicked.connect(self.buttonClicked2)
            bt2.show()
            j=j+1
            index=page*6+j
            bt3=QtGui.QPushButton(meta[index]+price[index],self)
            bt3.move(0,50)
            bt3.clicked.connect(self.buttonClicked3)
            bt3.show()
            j=j+1
            index=page*6+j
            bt4=QtGui.QPushButton(meta[index]+price[index],self)
            bt4.move(100,50)
            bt4.clicked.connect(self.buttonClicked4)
            bt4.show()
            j=j+1
            index=page*6+j
            bt5=QtGui.QPushButton(meta[index]+price[index],self)
            bt5.move(0,100)
            bt5.clicked.connect(self.buttonClicked5)
            bt5.show()
            j=j+1
            index=page*6+j     
            bt6=QtGui.QPushButton(meta[index]+price[index],self)
            bt6.move(100,100)
            bt6.clicked.connect(self.buttonClicked6)
            bt6.show()
	    
	    tabhost.show()
        except:
            QtGui.QMessageBox.information(self,'information','last page',QtGui.QMessageBox.Ok)
            j=0
            if j<last:
                index=page*6+j
                bt1=QtGui.QPushButton(meta[index],self)
                bt1.move(0,0)
                bt1.clicked.connect(self.buttonClicked1)
                bt1.show()
                j=j+1
            if j<last:
                index=page*6+j
                bt2=QtGui.QPushButton(meta[index],self)
                bt2.move(100,0)
                bt2.clicked.connect(self.buttonClicked2)
                bt2.show()
                j=j+1
            if j<last:
                index=page*6+j
                bt3=QtGui.QPushButton(meta[index],self)
                bt3.move(0,50)
                bt3.clicked.connect(self.buttonClicked3)
                bt3.show()
                j=j+1
            if j<last:
                index=page*6+j
                bt4=QtGui.QPushButton(meta[index],self)
                bt4.move(100,50)
                bt4.clicked.connect(self.buttonClicked4)
                bt4.show()
                j=j+1
            if j<last:
                index=page*6+j
                bt5=QtGui.QPushButton(meta[index],self)
                bt5.move(0,100)
                bt5.clicked.connect(self.buttonClicked5)
                bt5.show()
                j=j+1          
        if page!=0:
            btprior=QtGui.QPushButton('prior',self)
        else :
            btprior=QtGui.QPushButton('prior',self)
            btprior.setDisabled(True)
        if page!=maxpage:
            btnext=QtGui.QPushButton('next',self)
        else:
            btnext=QtGui.QPushButton('next',self)
            btnext.setDisabled(True)
        table=QtGui.QComboBox()
        table.itemData=tb
        table.move(250,0)
        table.show()        
        btprior.move(0,150)
        btprior.clicked.connect(self.buttonClicked7)      
        btnext.move(100,150)
        btnext.clicked.connect(self.buttonClicked8)        
        btsend=QtGui.QPushButton('send',self)
        btsend.move(200,200)
        btsend.clicked.connect(self.buttonClicked9)
        btprior.show()
        btnext.show()
        btsend.show()
        self.show()
    def fetch_data(self,arg1): #read name and price from database
        sconn=sqlite3.connect("new_sq.db")
        sconn.text_factory = sqlite3.OptimizedUnicode
        su=sconn.cursor()
	if arg1!=2:
	    #print "select * from name where family='%d';"%(arg1)
	    su.execute("select * from name where family=%d;"%(arg1))
	else:
	    print 'aa'
        global meta
        global index
        global price
        for r in su:
            assert type(r[0]) is str
            #assert type(r[1]) is int
            meta.append(r[0])
            price.append(r[1])
        index=0       
    def login(self):
        text, ok = QtGui.QInputDialog.getText(self, 'Input username','Enter your name:')
        if ok:
            global username
            username=(str)(text)
            if username != '':
                self.auth(username) #tcp conncetion test
                self.statusBar().showMessage('Ready')
            else:
                self.statusBar().showMessage('NO username input')
            print username
        else:
            self.statusBar().showMessage('NO username input')
    def auth(self,n):
        try:
	    global cport
            global address
            s = socket(AF_INET,SOCK_STREAM)
            s.connect((address,cport))
            s.send("\xab\xcd")  
            print s.recv(1024)
            s.close()
            QtGui.QMessageBox.information(self,'accept','login correct',QtGui.QMessageBox.Ok)
        except:
            QtGui.QMessageBox.warning(self,'alert','connection error',QtGui.QMessageBox.Ok)
            print 'connection error!'        
    def send(self,o,t,u): #o is order ,t is table ,u is username
        try:
	    global cport
            s = socket(AF_INET,SOCK_STREAM)
            s.connect((address,cport))
            string=''
            for i in range(0,len(o)):
                string+=o[i]
                string+=','
            print string
            ret = QtGui.QMessageBox.question(self, "commit",
                                 "you are going to commit?",
                                 QtGui.QMessageBox.Yes,
                                 QtGui.QMessageBox.Cancel)
            if ret == QtGui.QMessageBox.Yes:
                for i in range(0,len(o)):
                    order.pop()
                string+=t
		string+=","
		string+=u
		s.send(string)  
                print s.recv(1024)
                s.close()
                QtGui.QMessageBox.information(self,'accept','commited',QtGui.QMessageBox.Ok)
            else :
                return                 
        except:
            QtGui.QMessageBox.warning(self,'alert','connection error',QtGui.QMessageBox.Ok)
            print 'connection error!'
    def printarray(self):
        for i in range(0,len(order)):
            print order[i]
    def buttonClicked1(self):
        source=self.sender()
        order.append(source.text())
        self.printarray()
    def buttonClicked2(self):
        source=self.sender()
        order.append(source.text())
        self.printarray()
    def buttonClicked3(self):
        source=self.sender()
        order.append(source.text())
        self.printarray()
    def buttonClicked4(self):
        source=self.sender()
        order.append(source.text())
        self.printarray()
    def buttonClicked5(self):
        source=self.sender()
        order.append(source.text())
        self.printarray()
    def buttonClicked6(self):
        source=self.sender()
        order.append(source.text())
        self.printarray()    
    def buttonClicked7(self):
        global page
        if page>0:
            page=page-1
        self.initUI(page)
    def buttonClicked8(self):
        global page
        global maxpage
        global meta
        maxpage=len(meta)/6
        if page<maxpage:
            page=page+1
        self.initUI(page)       
    def buttonClicked9(self): # commit order
        global order
        print order
        self.send(order, 1, username)
    def downloadsql(self): # download database from server
        try:
            global fport
            ADDR = (address,fport)
            BUFSIZE = 1024
            FILEINFO_SIZE=struct.calcsize('128s32sI8s')
            conn = socket(AF_INET,SOCK_STREAM)
            conn.connect(ADDR)
            conn.send("\x00\x00")
	    while 1:
            	fhead = conn.recv(FILEINFO_SIZE)
            	filename,temp1,filesize,temp2=struct.unpack('128s32sI8s',fhead)
           	print filename,len(filename),type(filename)
            	print filesize
            	filename = filename.strip('\00')
            	fp = open(filename,'wb')
            	restsize = filesize
            	print "starting receive... ",
            	while 1:
                	if restsize > BUFSIZE:
                    		filedata = conn.recv(BUFSIZE)
                	else:
                    		filedata = conn.recv(restsize)
                	if not filedata: 
                    		break
                	fp.write(filedata)
                	restsize = restsize-len(filedata)
                	if restsize == 0:
                    		break
            print "finished..."
            fp.close()
            conn.close()
            print "closed..."
        except Exception,e:
            print e
def main():
    app = QtGui.QApplication(sys.argv)
    ex = qmain()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
