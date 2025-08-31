from tkinter import *
from PIL import ImageTk
import PIL.Image as PilImage

class View:

    zoomscale = 1
    timescale = 0.005
    maxsteps = 1280000
    minsteps = 25

    xtotal = 0
    ytotal = 0

    xstart = 0
    ystart = 0

    def __init__(self,window,canvas,focusbody,calc,display,edit,collisions,center,bodies,trails,keys):
        self.window = window
        self.canvas = canvas
        self.focusbody = focusbody
        self.calc = calc
        self.display = display
        self.edit = edit
        self.collisions = collisions
        self.center = center
        self.bodies = bodies
        self.trails = trails
        self.keys = keys

        # self.img = PilImage.open('C:\\Users\\eshan\\OneDrive - Reddy\\VS code\\Python\\Orbit_basic\\background.png')
        # self.img = self.img.resize((800,800), PilImage.Resampling.LANCZOS)
        # self.bg = ImageTk.PhotoImage(self.img)
        # self.canvas.create_image(-100,-100,image=self.bg,anchor="nw")

        self.resetbutton = Button(self.window,text="Reset",command=self.reset)
        self.resetbutton.place(x=755,y=12)

        self.window.bind("<Button-1>", self.click)
        self.window.bind("<B1-Motion>", self.motion)
        self.window.bind("<MouseWheel>", self.zoom)

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

    def insidebox(self,event):
        boxcoords = self.canvas.coords(self.edit.posbox)
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)
        if x > boxcoords[0]-10 and x < boxcoords[2]+10 and y > boxcoords[1]-10 and y < boxcoords[3]+10:
            return True
        return False
    
    def insidearrow(self,event):
        velcoords = self.canvas.coords(self.edit.velarrow)
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)
        if x > velcoords[2]-self.edit.boxsize-10 and x < velcoords[2]+self.edit.boxsize+10 and y > velcoords[3]-self.edit.boxsize-10 and y < velcoords[3]+self.edit.boxsize+10:
            return True
        return False

    def motion(self,event):
        if self.insidearrow(event) and self.edit.pause:
            self.edit.movevelarrow(event.x-self.xstart, event.y-self.ystart)
            self.display.updatevelocity()
        elif self.insidebox(event) and self.edit.pause:
            self.edit.moveposbox(event.x-self.xstart, event.y-self.ystart)
            self.display.updateposition()
        else:
            self.drag(event)
        self.xstart = event.x
        self.ystart = event.y

    def horizontalshift(self,factor):
        self.center[0] += factor
        self.canvas.xview_scroll(factor,"units")

    def verticalshift(self,factor):
        self.center[1] += factor
        self.canvas.yview_scroll(factor,"units")

    def click(self,event):
        self.xstart = event.x
        self.ystart = event.y

    def drag(self,event):
        self.horizontalshift(self.xstart-event.x)
        self.verticalshift(self.ystart-event.y)
        self.xstart = event.x
        self.ystart = event.y

    def adjustzoom(self,factor,x,y):
        for trail in self.trails.values():
            trail.rescale(factor, self.center)

        self.zoomscale *= factor
        self.calc.SCALE = 1000000000/self.zoomscale
        self.canvas.scale("moveable", x, y, factor, factor)

        self.collisions.zoomscale = self.zoomscale
        self.display.zoomscale = self.zoomscale
        self.edit.updatesizes()

    def zoom(self,event):
        if event.delta >= 0:
            self.adjustzoom(1.05,self.center[0],self.center[1])
        elif event.delta < 0:
            self.adjustzoom(0.95238,self.center[0],self.center[1])


