"""A few years back Gnome added an option to control whether menus could
have icons or if all the icons are ignored.  For a while at least that
option defaulted to ignoring the icons.  That default may have changed
since then but I haven't checked in a long time, IIRC you can edit it
with the gconf tool. 

gconftool-2 --type boolean --set /desktop/gnome/interface/
menus_have_icons true
"""


#!/usr/bin/env python

"""
ZetCode wxPython tutorial

In this example, we manually create
a menu item.

author: Jan Bodnar
website: www.zetcode.com
last modified: July 2020
"""

import wx

APP_EXIT = 1


class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):

        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        qmi = wx.MenuItem(fileMenu, APP_EXIT, '&Quit\tCtrl+Q')
        qmi.SetBitmap(wx.Bitmap('exit.ico'))
        fileMenu.Append(qmi)

        self.Bind(wx.EVT_MENU, self.OnQuit, id=APP_EXIT)

        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)

        self.SetSize((350, 250))
        self.SetTitle('Icons and shortcuts')
        self.Centre()
        
    def OnQuit(self, e):
        self.Close()


def main():

    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
