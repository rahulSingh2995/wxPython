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

        mpnl = MyPanel(self)


        self.SetTitle('wxSmartPhone')
        self.Centre()

def main():

    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
