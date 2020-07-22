#!/usr/bin/env python3 wxSmartPhone.py

"""

This is a Bluetooth Tester

author: Rahul Kumar
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

class MyTabs(wx.Frame):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        
        p = wx.Panel(self)
        nb = wx.Notebook(p)

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
        sizer = wx.BoxSizer()
        sizer.Add(nb, 1, wx.EXPAND)
        p.SetSizer(sizer)

class SecondPanel(wx.Frame):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)



class Example(wx.Frame):

    def __init__(self, *args, **kw):
        super(Example, self).__init__(*args, **kw)

        self.InitUI()


    def InitUI(self):
   
        """mainPnl = wx.Panel(self)
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        vbox1 = wx.BoxSizer(wx.VERTICAL)
        aboutBtn = wx.Button(mainPnl,label = "About")
        hcioBtn = wx.Button(mainPnl,label = "hcio")

        vbox1.Add(aboutBtn)
        vbox1.Add(hcioBtn)

        vbox2 = wx.BoxSizer(wx.VERTICAL)
        self.scdPnl = SecondPanel(self)
        vbox2.Add(self.scdPnl)

        hbox.Add(vbox1, wx.ALIGN_LEFT)
        hbox.Add(vbox2,proportion=1)

        mainPnl.SetSizer(hbox)

        hcioBtn.Bind(wx.EVT_BUTTON, self.onHcioClick)
        

        self.SetTitle('wxSmartPhone')
        self.Centre()
        self.SetSize(600,800)
        self.SetPosition((650,150))


    def onHcioClick(self,e):
        obj = MyTabs(self.scdPnl)
        """
    

def main():

    app = wx.App()
    ex = Example(None)
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
