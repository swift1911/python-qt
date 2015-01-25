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

#end
class qmain(QtGui.QMainWindow):    
    def __init__(self):
        super(qmain, self).__init__()
        self.login()
        self.initUI()
    def initUI(self):   
        self.resize(320,240)
        self.move(0,0)
        self.setWindowTitle('canteen order system') 
        usr=QtGui.QLabel(username)
        usr.move(300,0)
        usr.show()
        bt1=QtGui.QPushButton('model 1',self)
        bt1.move(0,0)
        bt1.clicked.connect(self.buttonClicked1)
        bt2=QtGui.QPushButton('model 2',self)
        bt2.move(100,0)
        bt2.clicked.connect(self.buttonClicked2)
        bt3=QtGui.QPushButton('model 3',self)
        bt3.move(0,50)
        bt3.clicked.connect(self.buttonClicked3)
        bt4=QtGui.QPushButton('model 4',self)
        bt4.move(100,50)
        bt4.clicked.connect(self.buttonClicked4)
        bt5=QtGui.QPushButton('model 5',self)
        bt5.move(0,100)
        bt5.clicked.connect(self.buttonClicked5)
        bt6=QtGui.QPushButton('model 6',self)
        bt6.move(100,100)
        bt6.clicked.connect(self.buttonClicked6)
        btprior=QtGui.QPushButton('prior',self)
        btprior.move(0,150)
        btprior.clicked.connect(self.buttonClicked7)
        btnext=QtGui.QPushButton('next',self)
        btnext.move(100,150)
        btnext.clicked.connect(self.buttonClicked7)        
        btsend=QtGui.QPushButton('send',self)
        btsend.move(200,200)
        btsend.clicked.connect(self.buttonClicked8)
        bt1.show()
        bt2.show()
        bt3.show()
        bt4.show()
        bt5.show()
        bt6.show()
        btprior.show()
        btnext.show()
        btsend.show()
        self.show()
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
            s.connect(("192.168.1.101", 22))
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
            s.connect(("192.168.1.101", 22))
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
        source=self.sender()
        order.append(source.text())
        self.printarray()
    def buttonClicked8(self):
        global order
        print order
        self.send(order, 1, username)
def main():
    app = QtGui.QApplication(sys.argv)
    ex = qmain()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
