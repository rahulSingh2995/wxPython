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
        
class RightPanel(wx.Panel):
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent)

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None)
 
        splitter = wx.SplitterWindow(self)
        leftP = LeftPanel(splitter)
        rightP = RightPanel(splitter)
        
        aboutBtn = wx.Button(leftP, label = "About")
        hcioBtn = wx.Button(leftP, label = "hcio")

        hcioBtn.Bind(wx.EVT_BUTTON, self.onHcioBtnClick)

        vbox1 = wx.BoxSizer(wx.VERTICAL)

        vbox1.Add(aboutBtn, 0, wx.EXPAND)
        vbox1.Add(hcioBtn, 0, wx.EXPAND)
        leftP.SetSizer(vbox1)

        #split the window
        splitter.SplitVertically(leftP, rightP)
        splitter.SetMinimumPaneSize(80)
        
        # Create notebook (tabs holder)
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
        vbox2 = wx.BoxSizer()
        vbox2.Add(nb, 1, wx.EXPAND)

        rightP.SetSizer(vbox2)
        leftP.SetFocus()

        splitter.SplitVertically(leftP, rightP)
        splitter.Unsplit()

        self.SetTitle('wxSmartPhone')
        self.SetSize(600,800)
        self.SetPosition((650,150))

    def onHcioBtnClick(self, e):
        self.splitter.SplitVertically(self.panelLeft, self.panelRight)
        self.splitter.SetMinimumPaneSize(20)
        self.panelLeft.SetFocus()

def main():
    app = wx.App(False)
    frame = MyFrame()
    frame.Show()
    app.MainLoop()

if __name__ == "__main__":
    main()
