# coding=utf-8
# 客户端

import threading
from socket import *
from tkinter import *


class tcpclient():
    def __init__(self):
        self.Host = 'localhost'
        self.Port = 21567
        self.BUFSIZ = 1024
        self.ADDR = (self.Host, self.Port)
        self.tcpsock = socket(AF_INET, SOCK_STREAM)
        self.tcpsock.connect(self.ADDR)
        self.top1 = Tk()
        self.label_name = Label(self.top1, text='username')
        self.top1.geometry('300x300')
        self.label_name.place(x=10, y=70, width=70, height=40)
        self.entry = Entry(self.top1, width=25)
        self.entry.place(x=80, y=70, height=40, width=200)
        self.buton = Button(self.top1, text='登陆', command=self.login_in)
        self.buton.place(x=200, y=150, width=60, height=30)
        self.top1.mainloop()

    # 登陆界面
    def login_in(self):
        text = self.entry.get()  # 输入用户名
        self.tcpsock.send(text.encode('utf-8'))
        self.top1.destroy()
        self.top2 = Tk()  # 选择聊天室
        self.top2.geometry('300x300')
        self.private = Button(self.top2, text='private room')  # 私人聊天室
        self.private.place(x=30, y=100, width=100, height=100)
        self.public = Button(self.top2, text='public room', command=self.public_room)  # 公共聊天室
        self.public.place(x=170, y=100, width=100, height=100)
        self.top2.mainloop()

    # 进入聊天室界面
    def public_room(self):
        self.top2.destroy()
        # 发送进入公共聊天室请求
        self.tcpsock.send('public'.encode())
        self.top3 = Tk()
        self.top3.geometry('300x400')
        self.top3.title('public room')
        self.frame1 = Frame(self.top3, bg='red')
        self.textlist = Text(self.frame1)  # 聊天记录框
        self.textlist.pack()
        self.frame1.place(x=10, y=10, width=270)
        self.text_input = Text(self.top3, bg='white')  # 消息输入框
        self.text_input.place(x=10, y=250, height=100, width=270)
        self.send_button = Button(self.top3, text='send', command=self.send_massage)  # 发送按钮
        self.send_button.place(x=250, y=370)
        threading.Thread(target=self.rec_message, args=()).start()
        self.top3.mainloop()

    # 发送消息
    def send_massage(self):
        self.massage = self.text_input.get('0.0', 'end')
        self.tcpsock.send(self.massage.encode('utf-8'))
        data = 'I:' + self.massage
        self.textlist.insert(END, data, )
        self.textlist.config(fg='red')
        self.text_input.delete('0.0', 'end')

    # 接收消息并显示
    def rec_message(self):
        while True:
            try:
                self.data = self.tcpsock.recv(self.BUFSIZ).decode('utf-8')
                self.textlist.insert(END, self.data, )
                self.textlist.config(fg='blue')
            except ConnectionError:
                print('error')


if __name__ == '__main__':
    a = tcpclient()
