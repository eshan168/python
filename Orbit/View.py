from tkinter import *

class View:

    zoomscale = 1
    timescale = 0.005
    maxsteps = 1280000
    minsteps = 25

    xtotal = 0
    ytotal = 0

    xstart = 0
    ystart = 0

    def __init__(self,window,canvas,focusbody,calc,display,center,bodies,trails,keys):
        self.window = window
        self.canvas = canvas
        self.focusbody = focusbody
        self.calc = calc
        self.display = display
        self.center = center
        self.bodies = bodies
        self.trails = trails
        self.keys = keys

        self.resetbutton = Button(self.window,text="Reset",command=self.reset)
        self.resetbutton.place(x=555,y=12)

    def reset(self):
        temp = list(self.keys)
        for key in temp:
            if key != "none":
                self.display.deletebody(key)

    def speedup(self):
        if self.calc.STEPS < self.maxsteps:
            self.calc.STEPS /= 0.5

    def slowdown(self):
        if self.calc.STEPS > self.minsteps:
            self.calc.STEPS /= 2

    def adjustzoom(self,factor,x,y):
        self.zoomscale *= factor
        self.calc.SCALE = 1000000000/self.zoomscale
        self.canvas.scale("all", x, y, factor, factor)
        self.display.zoomscale = self.zoomscale


    def zoom(self,event):
        for trail in self.trails.values():
            trail.skip()
        if event.delta >= 0:
            self.adjustzoom(1.05,self.center[0],self.center[1])
        elif event.delta < 0:
            self.adjustzoom(0.95238,self.center[0],self.center[1])
        for trail in self.trails.values():
            trail.updateprev()

    def changefocus(self,key):
        self.focusbody = self.bodies[key]
        coords = self.focusbody.getPosition()
        self.horizontalshift(int(coords[0]-self.center[0]))
        self.verticalshift(int(coords[1]-self.center[1]))

    def focus(self):
        if self.display.opt.get() != "none":
            if self.focusbody.key != self.display.opt.get():
                self.changefocus(self.display.opt.get())

            self.xtotal += self.focusbody.vector[0]*self.zoomscale*self.calc.STEPS
            self.ytotal += self.focusbody.vector[1]*self.zoomscale*self.calc.STEPS

            if abs(self.xtotal) > 1:
                xmove = int(self.xtotal)
                if self.xtotal > 0:    
                    self.horizontalshift(xmove)
                    self.xtotal -= xmove
                if self.xtotal < 0:    
                    self.horizontalshift(xmove)
                    self.xtotal -= xmove
            if abs(self.ytotal) > 1:
                ymove = int(self.ytotal)
                if self.ytotal > 0:    
                    self.verticalshift(ymove)
                    self.ytotal -= ymove
                if self.ytotal < 0:    
                    self.verticalshift(ymove)
                    self.ytotal -= ymove


    def horizontalshift(self,factor):
        self.center[0] += factor
        self.canvas.xview_scroll(factor,"units")

    def verticalshift(self,factor):
        self.center[1] += factor
        self.canvas.yview_scroll(factor,"units")

    def clickdown(self,event):
        self.xstart = event.x
        self.ystart = event.y

    def drag(self,event):
        self.horizontalshift(self.xstart-event.x)
        self.verticalshift(self.ystart-event.y)
        self.xstart = event.x
        self.ystart = event.y

