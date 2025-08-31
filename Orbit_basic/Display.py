from tkinter import *
from tkinter import ttk
import tkinter as tk
from decimal import Decimal
from Body import *
from Follower import *
from Calculations import *


class Display:

    SCALE = 1000000000
    zoomscale = 1
    scale = 100000000

    settingchoices = ["position","velocity","mass","name","color"]
    earthmass = 5.9722 * 10**24

    createy = [100,120]
    createx = 37
    teley = 350
    telex = 35
    buttonx = 50

    def __init__(self,window,canvas,calc,edit,bodies,trails,keys):
        self.window = window
        self.canvas = canvas
        self.calc = calc
        self.edit = edit
        self.bodies = bodies
        self.trails = trails
        self.keys = keys
        self.truekeys = list(self.keys[1:])

        self.scalecanvas = Canvas(window,width=100,height=30,bg="black",highlightthickness=0)
        self.scalecanvas.place(x=20,y=700)
        self.scaletext = self.scalecanvas.create_text(50,10,text=f"{round(self.scale/1000000,1)} million km",fill="white")
        self.Visual = self.scalecanvas.create_line(0,25,100,25,arrow=tk.BOTH,fill="white",width=1)


        self.frame = Frame(self.window,width=200,height=800,bg="#D0D0D0")
        self.frame.pack(side=LEFT)

        Label(self.frame,text="Focus:",font=("Arial",15),background="#D0D0D0").place(x=10,y=45)
        self.opt = StringVar(value=self.keys[0])
        self.options = OptionMenu(self.frame,self.opt,*self.keys)
        self.options.place(x=80,y=45)

        self.createbutton = Button(self.frame,text="Create",font=("Arial",12),width=10,command=self.start)
        self.createbutton.place(x=self.buttonx,y=self.createy[1]+10)

        Label(self.frame,text="earthmasses",font=("Arial",10),bg="#D0D0D0").place(x=self.createx+20,y=self.createy[0]+80)
        self.massEntry = Entry(self.frame)
        self.massEntry.place(x=self.createx,y=self.createy[1]+80)

        Label(self.frame,text="color",font=("Arial",10),bg="#D0D0D0").place(x=self.createx+45,y=self.createy[0]+130)
        self.colorEntry = Entry(self.frame)
        self.colorEntry.place(x=self.createx,y=self.createy[1]+130)

        Label(self.frame,text="name",font=("Arial",10),bg="#D0D0D0").place(x=self.createx+45,y=self.createy[0]+180)
        self.nameEntry = Entry(self.frame)
        self.nameEntry.place(x=self.createx,y=self.createy[1]+180)

        self.errortext = Label(self.frame,text="Invalid Input",fg="red",font=("Arial",15),bg="#D0D0D0")

        self.veltext = Label(self.frame,text=f"Velocity: {round(Calculations.velocity(self.edit.arrowtoboxvel())*self.SCALE,3)}m/s",font=("Arial",10),bg="#D0D0D0")
        self.postext = Label(self.frame,text=f"Distance: {round(self.edit.boxdistance(),3)}km",font=("Arial",10),bg="#D0D0D0")


        Label(self.frame,text="Body:",font=("Arial",15),background="#D0D0D0").place(x=10,y=self.teley+50)
        self.telemetrychoice = StringVar(value=self.truekeys[0])  
        self.telemetrychoices = OptionMenu(self.frame,self.telemetrychoice,*self.truekeys)
        self.telemetrychoices.place(x=75,y=self.teley+50)
        
        self.dstat = Label(self.frame,text="Distance:",font=("Arial",10),background="#D0D0D0")
        # self.dstat.place(x=telex,y=self.teley+100)
        self.vstat = Label(self.frame,text="Velocity:",font=("Arial",10),background="#D0D0D0")
        # self.vstat.place(x=telex,y=self.teley+125)
        self.xvstat = Label(self.frame,text="xvelocty:",font=("Arial",10),background="#D0D0D0")
        self.xvstat.place(x=self.telex,y=self.teley+100)
        self.yvstat = Label(self.frame,text="yvelocity:",font=("Arial",10),background="#D0D0D0")
        self.yvstat.place(x=self.telex,y=self.teley+125)
        self.xpstat = Label(self.frame,text="xposition:",font=("Arial",10),background="#D0D0D0")
        self.xpstat.place(x=self.telex,y=self.teley+150)
        self.ypstat = Label(self.frame,text="yposition:",font=("Arial",10),background="#D0D0D0")
        self.ypstat.place(x=self.telex,y=self.teley+175)
        self.mstat = Label(self.frame,text="mass:",font=("Arial",10),background="#D0D0D0")
        self.mstat.place(x=self.telex,y=self.teley+200)
        # self.cstat = Label(self.frame,text="centerbody:",font=("Arial",10),background="#D0D0D0")
        # self.cstat.place(x=15,y=self.teley+275)

        self.trailbutton = Button(self.frame,text="Delete Trail",font=("Arial",12),width=10,command=lambda: self.deletetrail(self.telemetrychoice.get()))
        self.trailbutton.place(x=self.buttonx,y=self.teley+250)

        self.deletebutton = Button(self.frame,text="Delete Body",font=("Arial",12),width=10,command=lambda: self.deletebody(self.telemetrychoice.get()))
        self.deletebutton.place(x=self.buttonx,y=self.teley+300)

    def updatemenus(self,keys):
        self.truekeys = list(self.keys[1:]) if len(keys) > 1 else keys

        val = self.opt.get() if self.opt.get() in self.keys else keys[0]
        self.opt = StringVar(value=val)
        self.options.destroy()
        self.options = OptionMenu(self.frame,self.opt,*self.keys)
        self.options.place(x=80,y=45)

        # val = self.centerbody.get() if self.centerbody.get() in self.keys else keys[0]
        # self.centerbody = StringVar(value=val)
        # self.centerbodies.destroy()
        # self.centerbodies = OptionMenu(self.frame,self.centerbody,*self.keys)
        # self.centerbodies.place(x=75,y=60)

        val = self.telemetrychoice.get() if self.telemetrychoice.get() in self.truekeys else self.truekeys[0]
        self.telemetrychoice = StringVar(value=val)
        self.telemetrychoices.destroy()
        self.telemetrychoices = OptionMenu(self.frame,self.telemetrychoice,*self.truekeys)
        self.telemetrychoices.place(x=75,y=self.teley+50)

    def start(self):

        try:
            xposition = self.canvas.canvasx(400)
            yposition = self.canvas.canvasy(400)
            xvelocity = 0
            yvelocity = 0
            name = self.nameEntry.get().lower()
            mass = float(eval(self.massEntry.get())) * self.earthmass
            diameter = Calculations.masstodiameter(float(eval(self.massEntry.get())))*self.zoomscale / 1000 / 2
            color = self.colorEntry.get().lower()
            self.keys.append(name)
            self.bodies[name] = Body(self.window,self.canvas,mass,diameter,xposition,yposition,xvelocity,yvelocity,color,name)
            self.updatemenus(self.keys)
        except (ValueError, SyntaxError, tk.TclError):
            self.errortext.place(x=45,y=self.createy[0]+240)
            return

        self.edit.boxbody = self.bodies[name]
        self.createbutton.configure(text="Finish", command=self.finish)
        self.errortext.place_forget()

        self.veltext.place(x=30,y=self.createy[0]+230)
        self.postext.place(x=30,y=self.createy[0]+260)
        self.edit.boxon()

    def finish(self):
        self.veltext.place_forget()
        self.postext.place_forget()
        self.createbutton.configure(text="Create", command=self.start)

        name = self.nameEntry.get().lower()
        self.trails[name] = Follower(self.window,self.canvas,name+"trail",self.bodies[name],self.calc,150)

        self.edit.boxbody.vector[0] = self.edit.boxvel[0]
        self.edit.boxbody.vector[1] = self.edit.boxvel[1]
        self.edit.boxoff()

    def updatevelocity(self):
        self.veltext.config(text=f"Velocity: {round(Calculations.velocity(self.edit.arrowtoboxvel())*self.SCALE,3)}m/s")

    def updateposition(self):
        self.postext.config(text=f"Distance: {round(self.edit.boxdistance(),3)}km")

    def deletebody(self,key):
        body = self.bodies[key]
        self.canvas.delete(body.body)
        self.keys.remove(key)
        if self.edit.boxbody == body:
            self.edit.boxbody = self.bodies["none"]

        # for body in self.bodies.values():
        #     if body.centerbody == key:
        #         body.centerbody = "none"
        self.deletetrail(key)

        self.updatemenus(self.keys)
        del self.bodies[key]
        del self.trails[key]
        self.opt.set("none")

    def deletetrail(self,key):
        trail = self.trails[key].trail
        self.canvas.delete(trail)

    def updatescale(self):
        self.scale = 100000000/self.zoomscale
        if self.scale < 1000000:
            self.scalecanvas.itemconfig(self.scaletext,text=f"{round(self.scale/1000,1)} thousand km")
        if self.scale >= 1000000 and self.scale < 1000000000:
            self.scalecanvas.itemconfig(self.scaletext,text=f"{round(self.scale/1000000,1)} million km")
        if self.scale >= 1000000000:
            self.scalecanvas.itemconfig(self.scaletext,text=f"{round(self.scale/1000000000,1)} billion km")

    def telemetry(self):
        body = self.bodies[self.telemetrychoice.get()]
        bodypos = body.getPosition()
        nonepos = self.bodies["none"].getPosition()
        self.dstat.config(text=f"Distance: {round(Body.distance(body,self.bodies["none"])/self.zoomscale,3)}")
        self.vstat.config(text=f"Velocity: {round(body.getVelocity(),3)}")
        self.xvstat.config(text=f"xvelocity: {round(body.vector[0]*1000000000,3)}")
        self.yvstat.config(text=f"yvelocity: {round(body.vector[1]*1000000000,3)}")
        self.xpstat.config(text=f"xposition: {round((bodypos[0]-nonepos[0])/self.zoomscale,3)}")
        self.ypstat.config(text=f"yposition: {round((bodypos[1]-nonepos[0])/self.zoomscale,3)}")
        self.mstat.config(text=f"mass: {"{:.4e}".format(Decimal(body.mass))}")
        
        