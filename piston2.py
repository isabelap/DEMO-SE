import wx
import time
from threading import Thread

class Piston(wx.Frame):
    
    def __init__(self, parent, id):
        
        #Frame width and height
        self.WIDTH = 800
        self.HEIGHT = 600

        
        wx.Frame.__init__(self,parent,id,'Piston',size=(self.WIDTH,self.HEIGHT),style= wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)

        #Panel
        self.panel = wx.Panel(self, size=(self.WIDTH, self.HEIGHT))

        #Stage label
        self.label=wx.StaticText(self.panel, -1, label='Stage 1', pos=(365,50))
        self.font = wx.Font(20, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        self.label.SetFont(self.font)

        start_process(self).start()

        self.Fit()
        



    def first_stage(self, event):
        #Establish the painting surface
        dc = wx.PaintDC(self.panel)
        
        dc.SetPen(wx.Pen('grey', 9))

        #Piston
        dc.DrawLine(270, 410, 550, 410) #Bottom line
        dc.DrawLine(270, 410, 270, 160) #Left line
        dc.DrawLine(550, 410, 550, 160) #Right line
        dc.DrawLine(290, 135, 530, 135) #Top line

        #Inside rectangle
        dc.SetPen(wx.Pen('black', 4))
        dc.SetBrush(wx.Brush('grey'))
        rect = wx.Rect(277, 300, 268, 60)
        dc.DrawRoundedRectangleRect(rect, 0)

        #Outside bottom rectangle
        dc.SetPen(wx.Pen('black', 4))
        dc.SetBrush(wx.Brush('grey'))
        rect2 = wx.Rect(383, 360, 60, 210)
        dc.DrawRoundedRectangleRect(rect2, 0)
        
        #Left top small piston
        dc.SetPen(wx.Pen('black', 3))
        dc.DrawLine(265, 134, 307, 175) #Thin line
        dc.SetPen(wx.Pen('black', 7))
        dc.DrawLine(298, 184, 317, 165) #Thick line

        #Right top small piston
        dc.SetPen(wx.Pen('black', 3))
        dc.DrawLine(580, 109, 539, 150) #Thin line
        dc.SetPen(wx.Pen('black', 7))
        dc.DrawLine(533, 140, 547, 157) #Thick line

    def second_stage(self, event):
        #Establish the painting surface
        dc = wx.PaintDC(self.panel)
        
        dc.SetPen(wx.Pen('grey', 9))

        #Piston
        dc.DrawLine(270, 410, 550, 410) #Bottom line
        dc.DrawLine(270, 410, 270, 160) #Left line
        dc.DrawLine(550, 410, 550, 160) #Right line
        dc.DrawLine(290, 135, 530, 135) #Top line

        #Inside rectangle
        dc.SetPen(wx.Pen('black', 4))
        dc.SetBrush(wx.Brush('grey'))
        rect = wx.Rect(277, 240, 268, 60)
        dc.DrawRoundedRectangleRect(rect, 0)

        #Outside bottom rectangle
        dc.SetPen(wx.Pen('black', 4))
        dc.SetBrush(wx.Brush('grey'))
        rect2 = wx.Rect(385, 300, 60, 210)
        dc.DrawRoundedRectangleRect(rect2, 0)
        
        #Left top small piston
        dc.SetPen(wx.Pen('black', 3))
        dc.DrawLine(241, 110, 283, 151) #Thin line
        dc.SetPen(wx.Pen('black', 7))
        dc.DrawLine(273, 159, 292, 140) #Thick line

        #Right top small piston
        dc.SetPen(wx.Pen('black', 3))
        dc.DrawLine(580, 109, 539, 150) #Thin line
        dc.SetPen(wx.Pen('black', 7))
        dc.DrawLine(533, 140, 547, 157) #Thick line

    def third_stage(self, event):
        #Establish the painting surface
        dc = wx.PaintDC(self.panel)
        
        dc.SetPen(wx.Pen('grey', 9))

        #Piston
        dc.DrawLine(270, 410, 550, 410) #Bottom line
        dc.DrawLine(270, 410, 270, 160) #Left line
        dc.DrawLine(550, 410, 550, 160) #Right line
        dc.DrawLine(290, 135, 530, 135) #Top line

        #Inside rectangle
        dc.SetPen(wx.Pen('black', 4))
        dc.SetBrush(wx.Brush('grey'))
        rect = wx.Rect(277, 190, 268, 60)
        dc.DrawRoundedRectangleRect(rect, 0)

        #Outside bottom rectangle
        dc.SetPen(wx.Pen('black', 4))
        dc.SetBrush(wx.Brush('grey'))
        rect2 = wx.Rect(385, 250, 60, 210)
        dc.DrawRoundedRectangleRect(rect2, 0)
        
        #Left top small piston
        dc.SetPen(wx.Pen('black', 3))
        dc.DrawLine(241, 110, 283, 151) #Thin line
        dc.SetPen(wx.Pen('black', 7))
        dc.DrawLine(273, 159, 292, 140) #Thick line

        #Right top small piston
        dc.SetPen(wx.Pen('black', 3))
        dc.DrawLine(580, 109, 539, 150) #Thin line
        dc.SetPen(wx.Pen('black', 7))
        dc.DrawLine(533, 140, 547, 157) #Thick line

        #Pressure point
        #============================
        #Circle
        dc.SetPen(wx.Pen('red', 3))
        dc.SetBrush(wx.Brush('red'))
        x = 414
        y = 165
        z = 10
        dc.DrawCircle(x,y,z)
        
        #Lines
        dc.DrawLine(380, 165, 405, 165)
        dc.DrawLine(420, 165, 445, 165)
        dc.DrawLine(415, 165, 445, 185)
        dc.DrawLine(413, 165, 395, 185)
        dc.DrawLine(400, 145, 420, 165)
        dc.DrawLine(428, 145, 415, 165)
        #============================

    def fourth_stage(self, event):
        #Establish the painting surface
        dc = wx.PaintDC(self.panel)
        
        dc.SetPen(wx.Pen('grey', 9))

        #Piston
        dc.DrawLine(270, 410, 550, 410) #Bottom line
        dc.DrawLine(270, 410, 270, 160) #Left line
        dc.DrawLine(550, 410, 550, 160) #Right line
        dc.DrawLine(290, 135, 530, 135) #Top line

        #Inside rectangle
        dc.SetPen(wx.Pen('black', 4))
        dc.SetBrush(wx.Brush('grey'))
        rect = wx.Rect(277, 240, 268, 60)
        dc.DrawRoundedRectangleRect(rect, 0)

        #Outside bottom rectangle
        dc.SetPen(wx.Pen('black', 4))
        dc.SetBrush(wx.Brush('grey'))
        rect2 = wx.Rect(385, 300, 60, 210)
        dc.DrawRoundedRectangleRect(rect2, 0)
        
        #Left top small piston
        dc.SetPen(wx.Pen('black', 3))
        dc.DrawLine(241, 110, 283, 151) #Thin line
        dc.SetPen(wx.Pen('black', 7))
        dc.DrawLine(273, 159, 292, 140) #Thick line

        #Right top small piston
        dc.SetPen(wx.Pen('black', 3))
        dc.DrawLine(580, 109, 539, 150) #Thin line
        dc.SetPen(wx.Pen('black', 7))
        dc.DrawLine(533, 140, 547, 157) #Thick line

    def fifth_stage(self, event):
        #Establish the painting surface
        dc = wx.PaintDC(self.panel)
        
        dc.SetPen(wx.Pen('grey', 9))

        #Piston
        dc.DrawLine(270, 410, 550, 410) #Bottom line
        dc.DrawLine(270, 410, 270, 160) #Left line
        dc.DrawLine(550, 410, 550, 160) #Right line
        dc.DrawLine(290, 135, 530, 135) #Top line

        #Inside rectangle
        dc.SetPen(wx.Pen('black', 4))
        dc.SetBrush(wx.Brush('grey'))
        rect = wx.Rect(277, 300, 268, 60)
        dc.DrawRoundedRectangleRect(rect, 0)

        #Outside bottom rectangle
        dc.SetPen(wx.Pen('black', 4))
        dc.SetBrush(wx.Brush('grey'))
        rect2 = wx.Rect(383, 360, 60, 210)
        dc.DrawRoundedRectangleRect(rect2, 0)
        
        #Left top small piston
        dc.SetPen(wx.Pen('black', 3))
        dc.DrawLine(241, 110, 283, 151) #Thin line
        dc.SetPen(wx.Pen('black', 7))
        dc.DrawLine(273, 159, 292, 140) #Thick line

        #Right top small piston
        dc.SetPen(wx.Pen('black', 3))
        dc.DrawLine(556, 133, 515, 174) #Thin line
        dc.SetPen(wx.Pen('black', 7))
        dc.DrawLine(508, 165, 522, 182) #Thick line
        
class start_process(Thread):
    def __init__(self, piston):
        Thread.__init__(self)
        self.piston = piston
        
    def run(self):
        for i in range(0,5):
            if i==0:
                self.piston.panel.Bind(wx.EVT_PAINT, self.piston.first_stage)
                self.piston.Refresh()
                time.sleep(3)
            elif i==1:
                
                self.piston.label.SetLabel("Stage 2")
                self.piston.panel.Bind(wx.EVT_PAINT, self.piston.second_stage)
                self.piston.Refresh()
                time.sleep(3)

            elif i==2:
                self.piston.label.SetLabel("Stage 3")
                self.piston.panel.Bind(wx.EVT_PAINT, self.piston.third_stage)
                self.piston.Refresh()
                time.sleep(3)

            elif i==3:
                self.piston.label.SetLabel("Stage 4")
                self.piston.panel.Bind(wx.EVT_PAINT, self.piston.fourth_stage)
                self.piston.Refresh()
                time.sleep(3)

            elif i==4:
                self.piston.label.SetLabel("Stage 1\'")
                self.piston.panel.Bind(wx.EVT_PAINT, self.piston.fifth_stage)
                self.piston.Refresh()
                time.sleep(3)
                

if __name__=='__main__':
    app=wx.App() 
    frame=Piston(parent=None,id=-1)
    frame.Show()
    frame.Centre()
    app.MainLoop()
