#! usr/bin/python simpleApp.py

import wx

class MyFrame(wx.Frame):
    def __init__(self,parent=None,title="Love",pos=(300,400), size=(400,600)):
        super().__init__(parent,title,pos,size)


if __name__ == "__main__":
    app = wx.App()
    frameObj = MyFrame()
    frameObj.show()
    app.MainLoop()
