import tkinter as tk
from Calculations import *


class Edit:

    arrowscale = 2

    def __init__(self,window,canvas,focusbody,calc,center,bodies,trails,keys):
        self.window = window
        self.canvas = canvas
        self.focusbody = focusbody
        self.calc = calc
        self.center = center
        self.bodies = bodies
        self.trails = trails
        self.keys = keys
        self.pause = False

        self.boxbody = bodies["earth"]
        self.boxsize = 15
        coords = self.boxbody.getPosition()
        self.posbox = self.canvas.create_rectangle(coords[0]-self.boxsize,coords[1]-self.boxsize,coords[0]+self.boxsize,coords[1]+self.boxsize,outline="white",width="3",state="hidden")

        self.velscale = 2000000 *self.arrowscale
        self.boxvel = self.boxbody.vector
        self.velarrow = self.canvas.create_line(coords[0],coords[1],coords[0]+self.boxvel[0]*self.velscale,coords[1]+self.boxvel[1]*self.velscale,arrow=tk.LAST,fill="white",width="3",state="hidden")

    def boxdistance(self):
        center = self.bodies["none"].getPosition()
        boxcenter = self.boxcoords()
        return Calculations.distance(center,boxcenter)

    def boxveltoarrow(self):
        return [self.velscale*self.boxvel[0],self.velscale*self.boxvel[1]]
    
    def arrowtoboxvel(self):
        coords = self.canvas.coords(self.velarrow)
        return [(coords[2]-coords[0])/self.velscale,(coords[3]-coords[1])/self.velscale]

    def updatesizes(self):
        bodycoords = self.boxbody.getPosition()
        diff = self.boxveltoarrow()
        self.canvas.coords(self.posbox,bodycoords[0]-self.boxsize,bodycoords[1]-self.boxsize,bodycoords[0]+self.boxsize,bodycoords[1]+self.boxsize)
        self.canvas.coords(self.velarrow,bodycoords[0],bodycoords[1],bodycoords[0]+diff[0],bodycoords[1]+diff[1])

    def moveposbox(self, x, y):
        self.canvas.move(self.posbox,x,y)
        self.canvas.move(self.velarrow,x,y)
        self.boxbody.move(x,y)

    def movevelarrow(self, x, y):
        boxcoords = self.boxcoords()

        velcoords = self.arrowcoords()
        xend = velcoords[0]+x
        yend = velcoords[1]+y

        self.canvas.coords(self.velarrow,boxcoords[0],boxcoords[1],xend,yend)
        self.boxvel = self.arrowtoboxvel()

    def boxon(self):
        self.pause = True
        self.updatesizes()
        self.canvas.itemconfig(self.posbox,state="normal")
        self.canvas.itemconfig(self.velarrow,state="normal")
    
    def boxoff(self):
        self.canvas.itemconfig(self.posbox,state="hidden")
        self.canvas.itemconfig(self.velarrow,state="hidden")
        self.pause = False

    def boxcoords(self):
        coords = self.canvas.coords(self.posbox)
        return [(coords[0]+coords[2])/2,(coords[1]+coords[3])/2]

    def arrowcoords(self):
        coords = self.canvas.coords(self.velarrow)
        return [coords[2],coords[3]]