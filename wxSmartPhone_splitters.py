#!/usr/bin/env python

"""
ZetCode wxPython tutorial

In this example, we create a help window window
with wx.html.HtmlWindow.

author: Jan Bodnar
website: www.zetcode.com
last modified: July 2020
"""

import wx

# Define the tab content as classes:
class TabOne(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        t = wx.StaticText(self, -1, "This is the first tab", (20,20))

class TabTwo(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        t = wx.StaticText(self, -1, "This is the second tab", (20,20))

class TabThree(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        t = wx.StaticText(self, -1, "This is the third tab", (20,20))

class TabFour(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        t = wx.StaticText(self, -1, "This is the last tab", (20,20))




class Example(wx.Frame):

    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)

        self.InitUI()

    def InitUI(self):

        self.splitter = wx.SplitterWindow(self)

        self.panelLeft = wx.Panel(self.splitter, wx.ID_ANY)
        #self.panelLeft = wx.Panel(self.splitter, wx.ID_ANY, style=wx.BORDER_SUNKEN)
        self.panelRight = wx.Panel(self.splitter)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        vbox1 = wx.BoxSizer(wx.VERTICAL)

        aboutBtn = wx.Button(self.panelLeft,label = "About")
        hcioBtn = wx.Button(self.panelLeft,label = "hcio")

        hcioBtn.Bind(wx.EVT_BUTTON, self.onHcioBtnClick)


        self.splitter.SplitVertically(self.panelLeft, self.panelRight)
        self.splitter.SetMinimumPaneSize(80)

        vbox1.Add(aboutBtn,0,wx.EXPAND)
        #vbox1.Add(aboutBtn)
        vbox1.Add(hcioBtn,0,wx.EXPAND)
        #vbox1.Add(hcioBtn)

        self.splitter.Unsplit()
        self.panelLeft.SetSizer(vbox1)


        # Create notebook (tabs holder)
        nb = wx.Notebook(self.panelRight)

        # Create the tab windows
        tab1 = TabOne(nb)
        tab2 = TabTwo(nb)
        tab3 = TabThree(nb)
        tab4 = TabFour(nb)

        # Add the windows to tabs and name them.
        nb.AddPage(tab1, "Tab 1")
        nb.AddPage(tab2, "Tab 2")
        nb.AddPage(tab3, "Tab 3")
        nb.AddPage(tab4, "Tab 4")

        # Set noteboook in a sizer to create the layout
        vbox2 = wx.BoxSizer()
        vbox2.Add(nb, 1, wx.EXPAND)

        self.panelRight.SetSizer(vbox2)
        self.panelLeft.SetFocus()


        self.SetTitle('wxSmartPhone')
        #self.Centre()
        self.SetSize(600,800)
        self.SetPosition((650,150))

    def onHcioBtnClick(self, e):
        self.splitter.SplitVertically(self.panelLeft, self.panelRight)
        self.splitter.SetMinimumPaneSize(80)
        self.panelLeft.SetFocus()

def main():

    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()

