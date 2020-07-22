import wx

# Define the tab content as classes:
class Wifi(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        t = wx.StaticText(self, -1, "This is the first tab", (20,20))
        self.SetSize=(30,10)

class Dongle(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add((-1, 10))
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)

        bluetoothName = wx.StaticText(self,-1,"   bluetooth address    ")
        infosBtn = wx.Button(self,label = "Infos")
        options = ["enabled","disabled"]
        comboBox = wx.ComboBox(self, choices = options)
        configBtn = wx.Button(self,label = "Config")

        hbox1.Add(bluetoothName,proportion=2,flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=32)
        hbox1.Add(infosBtn,proportion=0, flag= wx.EXPAND | wx.RIGHT, border=8)
        hbox1.Add(comboBox, proportion = 0, flag= wx.EXPAND |wx.RIGHT,border=8)
        hbox1.Add(configBtn, proportion = 0, flag=wx.EXPAND | wx.RIGHT,border=8)

        vbox.Add(hbox1)
        self.SetSizer(vbox)


class Phone(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        t = wx.StaticText(self, -1, "This is the third tab", (20,20))

class Contacts(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        t = wx.StaticText(self, -1, "This is the last tab", (20,20))

class SmsMms(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        t = wx.StaticText(self, -1, "This is the last tab", (20,20))

class Mail(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        t = wx.StaticText(self, -1, "This is the last tab", (20,20))

class Music(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        t = wx.StaticText(self, -1, "This is the last tab", (20,20))

class Media(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        t = wx.StaticText(self, -1, "This is the last tab", (20,20))

class Images(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        t = wx.StaticText(self, -1, "This is the last tab", (20,20))

class Videos(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        t = wx.StaticText(self, -1, "This is the last tab", (20,20))

class LeftPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        
        sizer = wx.BoxSizer(wx.VERTICAL)

        self.aboutBtn = wx.Button(self, label = "About")
        self.hcioBtn = wx.Button(self,label = "hcio")

        sizer.Add(self.aboutBtn, 0, wx.EXPAND)
        sizer.Add(self.hcioBtn, 0, wx.EXPAND)

        self.SetSizer(sizer)
    
class RightPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)

    def onAbtClicked(self):
        #self.SetBackgroundColour('#32CD32')
        #self.SetBackgroundColour('#b3b3b3')
        for child in self.GetChildren():
            child.Destroy()

        t = wx.StaticText(self, -1, "This is About tab", (40,20))


    def onHcioClicked(self):
        #self.SetBackgroundColour('#FF0000')
        for child in self.GetChildren():
            child.Destroy()

        nb = wx.Notebook(self,size=(510,765))

        # Create the tab windows
        wifiTab = Wifi(nb)
        dongleTab = Dongle(nb)
        phoneTab = Phone(nb)
        contactsTab = Contacts(nb)
        smsmmsTab = SmsMms(nb)
        mailTab = Mail(nb)
        musicTab = Music(nb)
        mediaTab = Media(nb)
        imagesTab = Images(nb)
        videosTab = Videos(nb)

        # Add the windows to tabs and name them.
        nb.AddPage(wifiTab, "Wifi")
        nb.AddPage(dongleTab, "Dongle")
        nb.AddPage(phoneTab, "Phone")
        nb.AddPage(contactsTab, "Contacts")
        nb.AddPage(smsmmsTab, "SMS/MMS")
        nb.AddPage(mailTab, "Mail")
        nb.AddPage(musicTab, "Music")
        nb.AddPage(mediaTab, "Media")
        nb.AddPage(imagesTab, "Images")
        nb.AddPage(videosTab, "Videos")

        # Set noteboook in a sizer to create the layout
        sizer = wx.BoxSizer()
        sizer.Add(nb, 1, wx.EXPAND)
        self.SetSizer(sizer)
        self.Update()

class MyForm(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="Splitter Tutorial")
 
        splitter = wx.SplitterWindow(self)
        self.leftP = LeftPanel(splitter)
        self.rightP = RightPanel(splitter)

        self.leftP.aboutBtn.Bind(wx.EVT_BUTTON, self.onAboutBtnClicked)    
        self.leftP.hcioBtn.Bind(wx.EVT_BUTTON, self.onHcioBtnClicked)

        # split the window
        splitter.SplitVertically(self.leftP, self.rightP)
        splitter.SetMinimumPaneSize(80)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(splitter,1, wx.EXPAND)
        self.SetSizer(sizer)

        self.SetTitle('wxSmartPhone')
        self.SetPosition((650,150))
        self.SetSize(600,800)

    def onAboutBtnClicked(self,e):
        self.rightP.onAbtClicked()
 
    def onHcioBtnClicked(self,e):
        self.rightP.onHcioClicked()
        #self.Maximize()
        #self.SetSize((600,800))


if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm()
    frame.Show()
    app.MainLoop()
