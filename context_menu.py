#!/usr/bin/env python

"""
ZetCode wxPython tutorial

In this example, we create a context menu.

author: Jan Bodnar
website: www.zetcode.com
last modified: July 2020
"""

import wx

class MyPopupMenu(wx.Menu):

    def __init__(self, parent):
        super(MyPopupMenu, self).__init__()

        self.parent = parent

        mmi = wx.MenuItem(self, wx.ID_ANY, 'Minimize')
        self.Append(mmi)
        self.Bind(wx.EVT_MENU, self.OnMinimize, mmi)

        cmi = wx.MenuItem(self, wx.ID_ANY, 'Close')
        self.Append(cmi)
        self.Bind(wx.EVT_MENU, self.OnClose, cmi)

        maxmi = wx.MenuItem(self, wx.ID_ANY, 'Maximize')
        self.Append(maxmi)
        self.Bind(wx.EVT_MENU, self.OnMaximize, maxmi)

    def OnMinimize(self, e):
        self.parent.Iconize()

    def OnMaximize(self, e):
        self.parent.Maximize()

    def OnClose(self, e):
        self.parent.Close()


class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):

        self.Bind(wx.EVT_RIGHT_DOWN, self.OnRightDown)
        #self.Bind(wx.EVT_LEFT_DOWN, self.OnRightDown)

        self.SetSize((350, 250))
        self.SetTitle('Context menu')
        self.Centre()

    def OnRightDown(self, e):
        #self.PopupMenu(MyPopupMenu(self), e.GetPosition())
        self.PopupMenu(MyPopupMenu(self), pos = (20,30))


def main():

    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()

