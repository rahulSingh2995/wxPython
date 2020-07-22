#!/usr/bin/env python3 wxSmartPhone.py

"""

This is a Bluetooth Tester

author: Rahul Kumar
last modified: July 2020
"""

import wx

class MyPanel(wx.Panel):

    def __init__(self, *args, **kw):
        super(MyPanel, self).__init__(*args, **kw)


class MyButton(wx.Button):

    def __init__(self, *args, **kw):
        super(MyButton, self).__init__(*args, **kw)

class Example(wx.Frame):

    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)

        self.InitUI()


    def InitUI(self):

        self.mpnl = MyPanel(self)

        self.hbox = wx.BoxSizer(wx.HORIZONTAL)

        self.vbox1 = wx.BoxSizer(wx.VERTICAL)
        self.aboutBtn = wx.Button(self.mpnl,label="About")
        self.hcioBtn = wx.Button(self.mpnl,label="hcio")
        self.vbox1.Add(self.aboutBtn)
        self.vbox1.Add(self.hcioBtn)

        self.vbox2 = wx.BoxSizer(wx.VERTICAL)

        self.hbox.Add(self.vbox1)
        self.hbox.Add(self.vbox2, proportion=1)
        self.mpnl.SetSizer(self.hbox)


        self.aboutBtn.Bind(wx.EVT_BUTTON, self.onAboutButton)

        self.SetTitle('wxSmartPhone')
        self.Centre()

        def onAboutButton(self,e):


def main():

    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
