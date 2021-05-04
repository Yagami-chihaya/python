# -*- coding:utf-8 -*-
from wxec import *
import wx


class Frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title='问诊机器人', size=(600, 500), name='frame', style=541072960)


        icon = wx.Icon(r'G:\python\WXpython\机器人.png')
        self.SetIcon(icon)

        self.openWindows = wx.Panel(self)
        self.openWindows.SetOwnBackgroundColour((255, 255, 255, 255))
        self.Centre()

        self.editFrame1 = wx.TextCtrl(self.openWindows, size=(444, 72), pos=(16, 340), value='', name='text',style=4096)
        editFrame1_font = wx.Font(12, 74, 90, 400, False, 'Microsoft YaHei UI', 28)
        self.editFrame1.SetFont(editFrame1_font)
        #self.editFrame1.Bind(wx.EVT_LEFT_DOWN, self.editFrame1_mouseClick_down)
        #self.editFrame1.Bind(wx.EVT_KILL_FOCUS, self.editFrame1_killFocus)

        self.button1 = wx.Button(self.openWindows, size=(80, 32), pos=(261, 423), label='关闭', name='button')
        self.button1.Bind(wx.EVT_LEFT_DOWN,self.button1_click)
        self.button2 = wx.Button(self.openWindows, size=(80, 32), pos=(352, 423), label='发送', name='button')
        self.button2.SetAuthNeeded(True)
        self.button2.SetForegroundColour((255, 255, 255, 255))
        self.button2.SetOwnBackgroundColour((24, 26, 52, 255))
        self.button2.Bind(wx.EVT_BUTTON,self.button2_click)


        self.editFrame2 = wx.TextCtrl(self.openWindows, size=(444, 166),pos=(119, 26),value='',name='text',style=4112)
        editFrame2_font = wx.Font(11, 74, 90, 400, False, 'Microsoft YaHei UI', 28)
        self.editFrame2.SetFont(editFrame2_font)
        self.editFrame2.SetOwnBackgroundColour((64, 128, 128, 255))


        robotPicture = wx.Image(r'G:\python\WXpython\机器人 (1).png').ConvertToBitmap()
        self.pictureFrame1 = wx_StaticBitmap(self.openWindows, bitmap=robotPicture, size=(111, 151), pos=(2, 14), name='staticBitmap',style=0)
        userPicture = wx.Image(r'G:\python\WXpython\用户.png').ConvertToBitmap()
        self.pictureFrame2 = wx_StaticBitmap(self.openWindows, bitmap=userPicture, size=(80, 73), pos=(487, 339), name='staticBitmap',style=0)

    def button2_click(self,event):
        saveData = self.editFrame1.Value
        self.editFrame2.Value=saveData
        print(saveData)

    def button1_click(self,event):
        quit()



class myApp(wx.App):
    def OnInit(self):
        self.frame = Frame()
        self.frame.Show(True)
        return True


if __name__ == '__main__':
    app = myApp()
    app.MainLoop()
