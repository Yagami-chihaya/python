#coding=utf-8
# 服务器端

from socket import *
import threading
import time

class tcpserve():
    def __init__(self):
        self.Host=''
        self.Port=21567
        self.BUFSIZ=1024
        self.ADDR=(self.Host,self.Port)
        self.tcpsock=socket(AF_INET,SOCK_STREAM)
        self.tcpsock.bind(self.ADDR)
        self.tcpsock.listen(5)
        self.doubleclients={}#群聊接入的客户列表
        self.singleclient={}#私人聊天室客户表
        self.client_socket={}#客户对应的嵌套字
        print('waiting for connection')
        self.tcp,self.addr=self.tcpsock.accept()
        print('connect from :',self.addr)
        self.usename=self.tcp.recv(self.BUFSIZ).decode('utf-8')
    def Deal(self,tcp,usename):

        data=tcp.recv(self.BUFSIZ).decode()
        if data=='public':
            #群聊
            while True:
                massage=tcp.recv(self.BUFSIZ).decode()
                #退出指令
                if massage=='quit':
                    del self.doubleclients[usename]
                    tcp.close()
                else:
                    for client in self.doubleclients:
                        self.doubleclients[client].send(('[%s] %s:%s'%(time.strftime('%Y/%m/%d %H:%M:%S',time.localtime()),usename,massage)).encode('utf-8'))
if __name__ == '__main__':
    tcpse=tcpserve()
    if not tcpse.doubleclients.__contains__(tcpse .usename):
        tcpse .doubleclients[tcpse.usename] = tcpse.tcp
        chat = threading.Thread(target=tcpse.Deal, args=(tcpse.tcp, tcpse.usename))
        chat.start()
    else:
        print('user is onlion')
