#!/usr/bin/env python

# moving.py

import wx


class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title,
            size=(300, 200))

        self.Move((800, 250))


def  main():

    app = wx.App()
    ex = Example(None,title = "Love")
    ex.Show()
    ex.Maximize()
    count =1
    count += 1
    if count == 100000:
        ex.Close()
    app.MainLoop()


if __name__ == '__main__':
    main()

