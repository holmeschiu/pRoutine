#!/usr/bin/python

import wx

class Motion(wx.Frame):
    def __init__(self, *args, **kw):
        super(Motion, self).__init__(*args, **kw)
        
        self.InitUI()
        
    def InitUI(self):
        pnl = wx.Panel(self)
        closeButton = wx.Button(pnl, label='Close', pos=(50, 50))
        closeButton.Bind(wx.EVT_BUTTON, self.OnClose)
        
        heading = wx.StaticText(self, label='Motion correction using MotionCor2', pos=(25, 15), size=(200, -1))
        
        self.SetSize((550, 550))
        self.SetTitle('Motion Correction')
        self.Centre()
    
    def OnClose(self, e):
        self.Close(True)
    

def main():
    app = wx.App()
    ex = Motion(None)
    ex.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()


