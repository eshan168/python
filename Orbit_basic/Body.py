import math
from View import *

class Body:

    SCALE = 1000000000
    SIZESCALE = 2

    def __init__(self,window,canvas,mass,radius,xposition,yposition,xv,yv,color,key):
        self.window = window
        self.canvas = canvas
        self.mass = mass
        self.radius = radius
        self.xposition = xposition
        self.yposition = yposition
        self.vector = [xv/self.SCALE,yv/self.SCALE]
        self.color = color
        self.body = canvas.create_oval(self.xposition-radius,self.yposition-radius,self.xposition+radius,self.yposition+radius,fill=color,tag="moveable")
        self.key = key

    def distance(a,b):
        a = a.getPosition()
        b = b.getPosition()
        return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

    def config(self,parameter,change):
        try:
            match parameter:
                case "color": self.canvas.itemconfig(self.body,fill=change)
                case "name": self.key = change
                case "xvelocity": self.vector[0] = int(change)/self.SCALE
                case "yvelocity": self.vector[1] = int(change)/self.SCALE
                case "xposition": self.canvas.moveto(self.body,int(change),self.getPosition()[1])
                case "yposition": self.canvas.moveto(self.body,self.getPosition()[0],int(change))
                case "mass": self.mass = int(eval(change))
        except ValueError:
            print("Not a parameter")

    def getPosition(self):
        temp = self.canvas.coords(self.body)
        return [(temp[0]+temp[2])/2, (temp[1]+temp[3])/2]
    
    def getVelocity(self):
        return math.sqrt(self.vector[0]**2 + self.vector[1]**2)*self.SCALE
    
    def move(self,x,y):
        self.canvas.move(self.body,x,y)



