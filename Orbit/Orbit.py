from tkinter import *
from Body import *
from Follower import *
from Masses import *
from Gravity import *
from View import *
from Display import *
import threading
import time


WIDTH = 600
HEIGHT = 600

CENTER = [300,300]
PAUSE = False

def pause(event):
    global PAUSE
    PAUSE = False if PAUSE else True
    if not PAUSE:
        threading.Thread(target=move,args=()).start()

def move():
    while not PAUSE:
        try:
            for body in bodies.values():
                if body.key != "none":
                    accel = calc.vector(bodies,body)
                    body.vector = [body.vector[0]+accel[0],body.vector[1]+accel[1]]
                    body.move(body.vector[0]*calc.STEPS*view.zoomscale,
                            body.vector[1]*calc.STEPS*view.zoomscale)

            view.focus()
            display.telemetry()
            display.updatescale()
            display.updateinputs()

            Follower.drawpaths(trails)
            time.sleep(view.timescale)
            window.update()

        # If dictionary changes size during loop
        except (RuntimeError,IndexError):
            continue


window = Tk()
window.geometry("806x603")
window.title("Orbit")

canvas = Canvas(window,width=WIDTH,height=HEIGHT,bg="black")
canvas.pack(side=LEFT)
canvas.configure(yscrollincrement="1")
canvas.configure(xscrollincrement="1")


calc = Gravity()
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
keys = [i.key for i in bodies]
trails = [Follower(window,canvas,i.key+"trail",i,calc,80) for i in bodies]

bodies = dict(zip(keys,bodies))
trails = dict(zip(keys,trails))

display = Display(window,canvas,calc,bodies,trails,keys)
view = View(window,canvas,none,calc,display,CENTER,bodies,trails,keys)

forward = Button(window,text="Faster",command=view.speedup)
forward.place(x=550,y=565)
backward = Button(window,text="Slower",command=view.slowdown)
backward.place(x=500,y=565)

window.bind("<MouseWheel>", view.zoom)
window.bind("<B1-Motion>", view.drag)
window.bind("<Button-1>", view.clickdown)
window.bind("<space>", pause)

threading.Thread(target=move,args=()).start()

window.mainloop()