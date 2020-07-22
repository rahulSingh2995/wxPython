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

class LeftPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        
        sizer = wx.BoxSizer(wx.VERTICAL)

        self.aboutBtn = wx.Button(self, label = "About")
        self.hcioBtn = wx.Button(self, label = "hcio")


        sizer.Add(self.aboutBtn, 0)
        sizer.Add(self.hcioBtn, 0)
        self.SetSizer(sizer)


class RightPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)

    def onHcioClick(self):
        nb = wx.Notebook(self)

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
        self.SetSizer(sizer)
    
class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="Splitter Tutorial")
 
        splitter = wx.SplitterWindow(self)
        self.leftP = LeftPanel(splitter)
        self.rightP = RightPanel(splitter)
        
        self.boolV = True

        # split the window
        splitter.SplitVertically(self.leftP, self.rightP)
        splitter.SetMinimumPaneSize(80)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(splitter, 1, wx.EXPAND)
        self.SetSizer(sizer)

        self.leftP.hcioBtn.Bind(wx.EVT_BUTTON, self.onHcioClick)

        self.SetTitle('wxSmartPhone')
        self.SetPosition((650,150))
        self.SetSize(600,800)
 
    def onHcioClick(self):
        if self.boolV:
            self.rightP.onHcioClick(self)
            boolV = False
        

def main():
    app = wx.App()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()

if __name__ == "__main__":
    main()
