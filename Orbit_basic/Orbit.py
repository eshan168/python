from tkinter import *
import threading
import time

from Body import *
from Follower import *
from Masses import *
from Calculations import *
from View import *
from Display import *
from Edit import *
from Collisions import *


WIDTH = 800
HEIGHT = 800

CENTER = [400,400]
PAUSE = False

def pause(event):
    global PAUSE
    PAUSE = not PAUSE
    
def run():
    if not PAUSE and not edit.pause:
        try:
            for body in bodies.values():
                if body.key != "none":
                    accel = calc.vector(bodies,body)
                    body.vector = [body.vector[0]+accel[0],body.vector[1]+accel[1]]
                    body.move(body.vector[0]*calc.STEPS*view.zoomscale,
                            body.vector[1]*calc.STEPS*view.zoomscale)
                    collisions.checkcollisions(body,bodies)

            view.focus()
            display.telemetry()
            display.updatescale()
            Follower.drawpaths(trails)
            try:
                print((mercury.radius+bodies["star"].radius),Body.distance(mercury,bodies["star"])/collisions.zoomscale)
            except:
                pass

        # If dictionary changes size during loop
        except (RuntimeError,IndexError):
            pass
        
    window.after(int(view.timescale * 1000), run)


window = Tk()
window.geometry("1006x803")
window.title("Orbit")

canvas = Canvas(window,width=WIDTH,height=HEIGHT,bg="black")
canvas.pack(side=LEFT)
canvas.configure(yscrollincrement="1")
canvas.configure(xscrollincrement="1")


calc = Calculations()
planets = Masses(window,canvas)

none = planets.getNone()
sun = planets.getSun()
mercury = planets.getMercury()
venus = planets.getVenus()
earth = planets.getEarth()
moon = planets.getMoon()
mars = planets.getMars()
jupiter = planets.getJupiter()
ganymede = planets.getGanymede()
europa = planets.getEuropa()
saturn = planets.getSaturn()
uranus = planets.getUranus()
neptune = planets.getNeptune()
triton = planets.getTriton()

bodies = [none,sun,mercury,venus,mars,earth,moon,jupiter,ganymede,europa,saturn,uranus,neptune,triton]
# bodies = [none,sun,earth,moon]
keys = [body.key for body in bodies]
trails = [Follower(window,canvas,body.key+"trail",body,calc,150) for body in bodies]

bodies = dict(zip(keys,bodies))
trails = dict(zip(keys,trails))

edit = Edit(window,canvas,none,calc,CENTER,bodies,trails,keys)
display = Display(window,canvas,calc,edit,bodies,trails,keys)
collisions = Collisions(window,canvas,keys,bodies,trails,display)
view = View(window,canvas,none,calc,display,edit,collisions,CENTER,bodies,trails,keys)

forward = Button(window,text=">>",command=view.speedup)
forward.place(x=765,y=715)
backward = Button(window,text="<<",command=view.slowdown)
backward.place(x=735,y=715)

window.bind("<space>", pause)
view.horizontalshift(-100)
view.verticalshift(-100)
run()

window.mainloop()