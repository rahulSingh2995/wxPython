#!/usr/bin/env python

"""
ZetCode wxPython tutorial

This example shows a simple menu.

author: Jan Bodnar
website: www.zetcode.com
last modified: July 2020
"""

import wx


class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):

        menubar = wx.MenuBar()

        fileMenu = wx.Menu()

        fileNewTab = fileMenu.Append(wx.ID_ANY, 'New Tab', 'Open a New Tab')
        self.Bind(wx.EVT_MENU,self.onNewTab,fileNewTab)

        fileNewWindow = fileMenu.Append(wx.ID_ANY, 'New Window', 'Open a New Window')

        fileCloseTab = fileMenu.Append(wx.ID_ANY, 'Close Tab', 'Close a Tab')
        self.Bind(wx.EVT_MENU, self.OnQuit, fileCloseTab)

        fileCloseWindow = fileMenu.Append(wx.ID_EXIT, 'Close Window', 'Close a Window')

        menubar.Append(fileMenu, '&File')


        editMenu = wx.Menu()
        editItem = editMenu.Append(wx.ID_ANY,"Copy","Copying")
        editItem = editMenu.Append(wx.ID_ANY,"Copy as HTML","Copying as HTML")
        editItem = editMenu.Append(wx.ID_ANY,"Paste","Paste here")
        editItem = editMenu.Append(wx.ID_ANY,"Select All","Click to select all")
        menubar.Append(editMenu, "&Edit")

        self.SetMenuBar(menubar)

        self.SetSize((900, 600))
        self.SetTitle('Application')
        self.Centre()

    def OnQuit(self, e):
        self.Close()

    def onNewTab(self,e):
        self.SetTitle("Faurecia")

def main():

    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
