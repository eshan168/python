from tkinter import *
from tkinter import ttk
import tkinter as tk
from decimal import Decimal
from Body import *
from Follower import *


class Display:

    zoomscale = 1
    scale = 100000000
    createy = [100,120]
    settingchoices = ["position","velocity","mass","name","color"]

    def __init__(self,window,canvas,calc,bodies,trails,keys):
        self.window = window
        self.canvas = canvas
        self.calc = calc
        self.bodies = bodies
        self.trails = trails
        self.keys = keys
        self.truekeys = list(self.keys[1:])
        self.pause = False


        self.scalecanvas = Canvas(window,width=100,height=30,bg="black",highlightthickness=0)
        self.scalecanvas.place(x=20,y=550)
        self.scaletext = self.scalecanvas.create_text(50,10,text=f"{round(self.scale/1000000,1)} million km",fill="white")
        self.Visual = self.scalecanvas.create_line(0,25,100,25,arrow=tk.BOTH,fill="white",width=1)

        tabs = ttk.Notebook(self.window)
        frame1 = Frame(tabs)
        frame2 = Frame(tabs)
        frame3 = Frame(tabs)

        tabs.add(frame1,text="Create") 
        tabs.add(frame2,text="Modify")
        tabs.add(frame3,text="Stats")
        tabs.pack(expand=1, fill="both", side=TOP) 


        self.createframe = Frame(frame1,width=200,height=600,bg="gray")
        self.createframe.pack(side=LEFT)

        Label(self.window,text="Focus:",font=("Arial",15),background="gray").place(x=610,y=35)
        self.opt = StringVar(value=self.keys[0])
        self.options = OptionMenu(self.window,self.opt,*self.keys)
        self.options.place(x=680,y=35)

        Label(self.createframe,text="Center:",font=("Arial",15),background="gray").place(x=4,y=60)
        self.centerbody = StringVar(value=self.keys[0])  
        self.centerbodies = OptionMenu(self.createframe,self.centerbody,*keys)
        self.centerbodies.place(x=75,y=60)

        Label(self.createframe,text="xposition (10^6 km)",font=("Arial",10),bg="gray").place(x=43,y=self.createy[0])
        self.xposEntry = Entry(self.createframe)
        self.xposEntry.place(x=40,y=self.createy[1])

        Label(self.createframe,text="yposition (10^6 km)",font=("Arial",10),bg="gray").place(x=43,y=self.createy[0]+50)
        self.yposEntry = Entry(self.createframe)
        self.yposEntry.place(x=40,y=self.createy[1]+50)

        Label(self.createframe,text="xvelocity (m/s)",font=("Arial",10),bg="gray").place(x=56,y=self.createy[0]+100)
        self.xvelEntry = Entry(self.createframe)
        self.xvelEntry.place(x=40,y=self.createy[1]+100)

        Label(self.createframe,text="yvelocity (m/s)",font=("Arial",10),bg="gray").place(x=56,y=self.createy[0]+150)
        self.yvelEntry = Entry(self.createframe)
        self.yvelEntry.place(x=40,y=self.createy[1]+150)

        Label(self.createframe,text="mass (kg)",font=("Arial",10),bg="gray").place(x=70,y=self.createy[0]+200)
        self.massEntry = Entry(self.createframe)
        self.massEntry.place(x=40,y=self.createy[1]+200)

        Label(self.createframe,text="diameter (10^3 km)",font=("Arial",10),bg="gray").place(x=43,y=self.createy[0]+250)
        self.diameterEntry = Entry(self.createframe)
        self.diameterEntry.place(x=40,y=self.createy[1]+250)

        Label(self.createframe,text="color",font=("Arial",10),bg="gray").place(x=85,y=self.createy[0]+300)
        self.colorEntry = Entry(self.createframe)
        self.colorEntry.place(x=40,y=self.createy[1]+300)

        Label(self.createframe,text="name",font=("Arial",10),bg="gray").place(x=85,y=self.createy[0]+350)
        self.nameEntry = Entry(self.createframe)
        self.nameEntry.place(x=40,y=self.createy[1]+350)

        self.createbutton = Button(self.createframe,text="Create",font=("Arial",15),command=self.create)
        self.createbutton.place(x=65,y=self.createy[1]+390)


        self.modifyframe = Frame(frame2,width=200,height=600,bg="gray")
        self.modifyframe.pack(side=LEFT)

        Label(self.modifyframe,text="Body:",font=("Arial",15),background="gray").place(x=5,y=75)
        self.modchoice = StringVar(value=self.truekeys[0])  
        self.modchoices = OptionMenu(self.modifyframe,self.modchoice,*self.truekeys)
        self.modchoices.place(x=75,y=75)
        self.prevmod = ""

        Label(self.modifyframe,text="Setting:",font=("Arial",15),background="gray").place(x=4,y=115)
        self.setting = StringVar(value=self.settingchoices[0])  
        self.settings = OptionMenu(self.modifyframe,self.setting,*self.settingchoices)
        self.settings.place(x=76,y=115)
        self.prevsetting = ""

        self.xtext = Label(self.modifyframe,text="xposition",font=("Arial",10),bg="gray")
        self.xtext.place(x=43,y=self.createy[0]+80)
        self.xchange = Entry(self.modifyframe)
        self.xchange.place(x=40,y=self.createy[1]+80)

        self.ytext = Label(self.modifyframe,text="yposition",font=("Arial",10),bg="gray")
        self.ytext.place(x=43,y=self.createy[0]+120)
        self.ychange = Entry(self.modifyframe)
        self.ychange.place(x=40,y=self.createy[1]+120)

        self.applybutton = Button(self.modifyframe,text="Apply",font=("Arial",10),width=10,command=self.modify)
        self.applybutton.place(x=58,y=275)

        self.trailbutton = Button(self.modifyframe,text="Delete Trail",font=("Arial",15),command=lambda: self.deletetrail(self.modchoice.get()))
        self.trailbutton.place(x=43,y=460)

        self.deletebutton = Button(self.modifyframe,text="Delete Body",font=("Arial",15),command=lambda: self.deletebody(self.modchoice.get()))
        self.deletebutton.place(x=40,y=510)

        
        self.telemetryframe = Frame(frame3,width=200,height=600,bg="gray")
        self.telemetryframe.pack(side=LEFT)

        Label(self.telemetryframe,text="Body:",font=("Arial",15),background="gray").place(x=5,y=75)
        self.telemetrychoice = StringVar(value=self.truekeys[0])  
        self.telemetrychoices = OptionMenu(self.telemetryframe,self.telemetrychoice,*self.truekeys)
        self.telemetrychoices.place(x=75,y=75)
        
        self.dstat = Label(self.telemetryframe,text="Distance:",font=("Arial",10),background="gray")
        self.dstat.place(x=10,y=120)
        self.vstat = Label(self.telemetryframe,text="Velocity:",font=("Arial",10),background="gray")
        self.vstat.place(x=10,y=160)
        self.xvstat = Label(self.telemetryframe,text="xvelocty:",font=("Arial",10),background="gray")
        self.xvstat.place(x=10,y=200)
        self.yvstat = Label(self.telemetryframe,text="yvelocity:",font=("Arial",10),background="gray")
        self.yvstat.place(x=10,y=240)
        self.xpstat = Label(self.telemetryframe,text="xposition:",font=("Arial",10),background="gray")
        self.xpstat.place(x=10,y=280)
        self.ypstat = Label(self.telemetryframe,text="yposition:",font=("Arial",10),background="gray")
        self.ypstat.place(x=10,y=320)
        self.mstat = Label(self.telemetryframe,text="mass:",font=("Arial",10),background="gray")
        self.mstat.place(x=10,y=360)
        self.cstat = Label(self.telemetryframe,text="centerbody:",font=("Arial",10),background="gray")
        self.cstat.place(x=10,y=400)

    def updatemenus(self,keys):
        self.truekeys = list(self.keys[1:]) if len(keys) > 1 else keys

        val = self.opt.get() if self.opt.get() in self.keys else keys[0]
        self.opt = StringVar(value=val)
        self.options.destroy()
        self.options = OptionMenu(self.window,self.opt,*self.keys)
        self.options.place(x=680,y=35)

        val = self.centerbody.get() if self.centerbody.get() in self.keys else keys[0]
        self.centerbody = StringVar(value=val)
        self.centerbodies.destroy()
        self.centerbodies = OptionMenu(self.createframe,self.centerbody,*self.keys)
        self.centerbodies.place(x=75,y=60)

        val = self.modchoice.get() if self.modchoice.get() in self.truekeys else self.truekeys[0]
        self.modchoice = StringVar(value=val)
        self.modchoices.destroy()
        self.modchoices = OptionMenu(self.modifyframe,self.modchoice,*self.truekeys)
        self.modchoices.place(x=75,y=75)

        val = self.telemetrychoice.get() if self.telemetrychoice.get() in self.truekeys else self.truekeys[0]
        self.telemetrychoice = StringVar(value=val)
        self.telemetrychoices.destroy()
        self.telemetrychoices = OptionMenu(self.telemetryframe,self.telemetrychoice,*self.truekeys)
        self.telemetrychoices.place(x=75,y=75)

    def create(self):
        try:
            name = self.nameEntry.get().lower()
            centerbody = self.bodies[self.centerbody.get()]
            centerbodypos = centerbody.getPosition()
            xposition = float(self.xposEntry.get())*self.zoomscale+centerbodypos[0]
            yposition = float(self.yposEntry.get())*self.zoomscale+centerbodypos[1]
            xvelocity = float(self.xvelEntry.get())+centerbody.vector[0]*1000000000
            yvelocity = float(self.yvelEntry.get())+centerbody.vector[1]*1000000000
            mass = float(eval(self.massEntry.get()))
            diameter = float(self.diameterEntry.get()) * self.zoomscale / 1000
            color = self.colorEntry.get().lower()
            new = Body(self.window,self.canvas,mass,diameter,xposition,yposition,xvelocity,yvelocity,centerbody.key,color,name)
            newtrail = Follower(self.window,self.canvas,name+"trail",new,self.calc,50)
            self.keys.append(name)
            self.updatemenus(self.keys)
            self.bodies[name] = new
            self.trails[name] = newtrail
        except (ValueError, SyntaxError, tk.TclError):
            print("Invalid input")

    def updateinputs(self):
        choice = self.modchoice.get()
        if choice != self.prevmod:
            if choice == "none":
                self.deletebutton.place_forget()
            else:
                self.deletebutton.place(x=40,y=510)
        self.prevmod = choice

        choice = self.setting.get()
        if choice != self.prevsetting:
            if choice == "velocity" or choice == "position":
                self.ychange.place(x=40,y=self.createy[1]+120)
                self.applybutton.place(x=58,y=275)
                if choice == "velocity":
                    self.ytext.place(x=56,y=self.createy[0]+120)
                    self.xtext.place(x=56,y=self.createy[0]+80)
                    self.xtext.config(text="xvelocity (m/s)")
                    self.ytext.config(text="yvelocity (m/s)")
                if choice == "position":
                    self.ytext.place(x=43,y=self.createy[0]+120)
                    self.xtext.place(x=43,y=self.createy[0]+80)
                    self.xtext.config(text="xposition (10^6 km)")
                    self.ytext.config(text="yposition (10^6 km)")
            if choice == "mass" or choice == "name" or choice == "color":
                self.ychange.place_forget()
                self.ytext.place_forget()
                self.xtext.place(x=84,y=self.createy[0]+80)
                self.applybutton.place(x=58,y=235)
                if choice == "mass":
                    self.xtext.config(text="mass")
                if choice == "name":
                    self.xtext.config(text="name")
                if choice == "color":
                    self.xtext.config(text="color")
        self.prevsetting = choice

    def modify(self):
        body = self.bodies[self.modchoice.get()]
        centerbody = self.bodies[body.centerbody]
        parameter = self.setting.get()

        try:
            if parameter == "position":
                centerbodypos = centerbody.getPosition()
                xposition = float(self.xchange.get())*self.zoomscale+centerbodypos[0]
                yposition = float(self.ychange.get())*self.zoomscale+centerbodypos[1]
                body.config("xposition",xposition)
                body.config("yposition",yposition)
            elif parameter == "velocity":
                xvelocity = float(self.xchange.get())+centerbody.vector[0]*1000000000
                yvelocity = float(self.ychange.get())+centerbody.vector[1]*1000000000
                body.config("xvelocity",xvelocity)
                body.config("yvelocity",yvelocity)
            else:
                body.config(parameter,self.xchange.get())

        except (ValueError, SyntaxError):
            print("Invalid input")

    def deletebody(self,key):
        body = self.bodies[key]
        trails = self.trails[key].trail
        self.canvas.delete(body.body)
        self.keys.remove(key)

        for body in self.bodies.values():
            if body.centerbody == key:
                body.centerbody = "none"
        for trail in trails:
            self.canvas.delete(trail)

        self.updatemenus(self.keys)
        del self.bodies[key]
        del self.trails[key]
        self.opt.set("none")

    def deletetrail(self,key):
        trails = self.trails[key].trail
        for trail in trails:
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
        centerbody = self.bodies[body.centerbody]
        bodypos = body.getPosition()
        centerbodypos = centerbody.getPosition()
        self.dstat.config(text=f"Distance: {round(Body.distance(body,centerbody)/self.zoomscale,3)}")
        self.vstat.config(text=f"Velocity: {round(body.getVelocity()-centerbody.getVelocity(),3)}")
        self.xvstat.config(text=f"xvelocity: {round((body.vector[0]-centerbody.vector[0])*1000000000,3)}")
        self.yvstat.config(text=f"yvelocity: {round((body.vector[1]-centerbody.vector[1])*1000000000,3)}")
        self.xpstat.config(text=f"xposition: {round((bodypos[0]-centerbodypos[0])/self.zoomscale,3)}")
        self.ypstat.config(text=f"yposition: {round((bodypos[1]-centerbodypos[1])/self.zoomscale,3)}")
        self.mstat.config(text=f"mass: {"{:.4e}".format(Decimal(body.mass))}")
        self.cstat.config(text=f"centerbody: {body.centerbody}")

    def getTelemetry(self):
        body = self.bodies[self.telemetrychoice.get()]
        centerbody = self.bodies[body.centerbody]
        bodypos = body.getPosition()
        centerbodypos = centerbody.getPosition()
        self.dstat.config(text=f"Distance: {round(Body.distance(body,centerbody)/self.zoomscale,3)}")
        self.vstat.config(text=f"Velocity: {round(body.getVelocity()-centerbody.getVelocity(),3)}")
        self.xvstat.config(text=f"xvelocity: {round((body.vector[0]-centerbody.vector[0])*1000000000,3)}")
        self.yvstat.config(text=f"yvelocity: {round((body.vector[1]-centerbody.vector[1])*1000000000,3)}")
        self.xpstat.config(text=f"xposition: {round((bodypos[0]-centerbodypos[0])/self.zoomscale,3)}")
        self.ypstat.config(text=f"yposition: {round((bodypos[1]-centerbodypos[1])/self.zoomscale,3)}")
        self.mstat.config(text=f"mass: {"{:.4e}".format(Decimal(body.mass))}")
        self.cstat.config(text=f"centerbody: {body.centerbody}")
        