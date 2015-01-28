#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import socket
import binascii
import ssl
import sqlite3
from PyQt4 import QtGui

#global varible

username=''
order=[]
spice=[]
meta=[]
index=0
page=0
maxpage=0

#end
class qmain(QtGui.QMainWindow):    
    def __init__(self):
        super(qmain, self).__init__()
        self.login()
        self.fetch_data()
        self.initUI(0)
    def initUI(self,p):  
        global index
        global page
        index=0
        j=0
        last=len(meta)/6-page*6
        maxpage=len(meta)/6
        self.resize(320,240)
        self.move(0,0)
        self.setWindowTitle('canteen order system') 
        usr=QtGui.QLabel(username)
        usr.move(150,0)
        usr.show()
        try:
            index=page*6+j
            bt1=QtGui.QPushButton(meta[index],self)
            bt1.move(0,0)
            bt1.clicked.connect(self.buttonClicked1)
            bt1.show()
            j=j+1
            index=page*6+j
            bt2=QtGui.QPushButton(meta[index],self)
            bt2.move(100,0)
            bt2.clicked.connect(self.buttonClicked2)
            bt2.show()
            j=j+1
            index=page*6+j
            bt3=QtGui.QPushButton(meta[index],self)
            bt3.move(0,50)
            bt3.clicked.connect(self.buttonClicked3)
            bt3.show()
            j=j+1
            index=page*6+j
            bt4=QtGui.QPushButton(meta[index],self)
            bt4.move(100,50)
            bt4.clicked.connect(self.buttonClicked4)
            bt4.show()
            j=j+1
            index=page*6+j
            bt5=QtGui.QPushButton(meta[index],self)
            bt5.move(0,100)
            bt5.clicked.connect(self.buttonClicked5)
            bt5.show()
            j=j+1
            index=page*6+j     
            bt6=QtGui.QPushButton(meta[index],self)
            bt6.move(100,100)
            bt6.clicked.connect(self.buttonClicked6)
            bt6.show()
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
    def fetch_data(self):
        sconn=sqlite3.connect("sq.db")
        sconn.text_factory = sqlite3.OptimizedUnicode
        su=sconn.cursor()
        su.execute("select * from name;")
        global meta
        global index
        for r in su:
            assert type(r[0]) is str
            meta.append(r[0])
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
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect(("192.168.1.101",22))
            s.send("\xab\xcd")  
            print s.recv(1024)
            s.close()
            QtGui.QMessageBox.information(self,'accept','login correct',QtGui.QMessageBox.Ok)
        except:
            QtGui.QMessageBox.warning(self,'alert','connection error',QtGui.QMessageBox.Ok)
            print 'connection error!'        
    def send(self,o,t,u):
        try:
            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect(("192.168.1.101",22))
            string=''
            for i in range(0,len(o)):
                string+=order[i]
                string+=','
            print string
            s.send(string)  
            print s.recv(1024)
            s.close()
            QtGui.QMessageBox.information(self,'accept','commited',QtGui.QMessageBox.Ok)
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
    def buttonClicked9(self):
        global order
        print order
        self.send(order, 1, username)
def main():
    app = QtGui.QApplication(sys.argv)
    ex = qmain()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
