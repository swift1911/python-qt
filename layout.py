#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import socket
import binascii
import ssl
import sqlite3
from PyQt4 import QtGui

global username
class qmain(QtGui.QMainWindow):
    
    def __init__(self):
        super(qmain, self).__init__()
        
        self.initUI()
    def initUI(self):   
        self.statusBar().showMessage('Ready')
        self.resize(320,240)
        self.move(0,0)
        self.setWindowTitle('canteen order system')  
        bt1=QtGui.QPushButton('model 1',self)
        bt1.move(0,0)
        bt1.clicked.connect(self.buttonClicked1)
        bt2=QtGui.QPushButton('model 2',self)
        bt2.move(100,0)
        bt3=QtGui.QPushButton('model 3',self)
        bt3.move(0,50)
        bt4=QtGui.QPushButton('model 4',self)
        bt4.move(100,50)
        bt5=QtGui.QPushButton('model 5',self)
        bt5.move(0,100)
        bt6=QtGui.QPushButton('model 6',self)
        bt6.move(100,100)
        bt7=QtGui.QPushButton('enter',self)
        bt7.move(150,150)
        bt1.show()
        bt2.show()
        bt3.show()
        bt4.show()
        bt5.show()
        bt6.show()
        bt7.show()
        self.show()
        text, ok = QtGui.QInputDialog.getText(self, 'Input username','Enter your name:')
        if ok:
            username=(str)(text)
            print username
    def send(self,args1,args2):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect(("192.168.1.101", 22))
        s.send("\xab\xcd")  # 前面为十六进制数据，后面可接字符串等正文
        print s.recv(1024)
        s.close()        
    def buttonClicked1(self):
        self.send('1',username)
        
def main():
    app = QtGui.QApplication(sys.argv)
    ex = qmain()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
