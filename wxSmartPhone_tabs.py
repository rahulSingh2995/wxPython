import wx

class About(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        #t = wx.StaticText(self, -1, "This is the About tab", (20,20))

class Hcio(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        #t = wx.StaticText(self, -1, "This is the hcio tab", (20,20))

class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="wxPython tabs example @pythonspot.com")

        # Create a panel and notebook (tabs holder)
        p = wx.Panel(self)
        nb = wx.Notebook(p,style=wx.NB_TOP)
        nbb = wx.Notebook(p,style=wx.NB_TOP)
        # Create the tab windows
        aboutTab = About(nb)
        hcioTab = Hcio(nbb)

        nb.AddPage(aboutTab, "Tab 1")
        nbb.AddPage(hcioTab, "Tab 2")

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(nb,1, wx.EXPAND)
        sizer.Add(nbb,1, wx.EXPAND)
        p.SetSizer(sizer)


if __name__ == "__main__":
    app = wx.App()
    MainFrame().Show()
    app.MainLoop()

