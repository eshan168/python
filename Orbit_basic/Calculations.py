import math
from Body import *

class Calculations:

    GCONSTANT = 6.67430 * 10**-11
    GRAVITYSCALE = 1000000000
    SCALE = 1000000000
    STEPS = 5000

    def distance(a,b):
        return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
    
    def velocity(vector):
        return math.sqrt(vector[0]**2 + vector[1]**2)

    def gravity(self,distance,mass):
        if distance == 0:
            distance = 0.00001
        return (self.GCONSTANT * (mass)/(distance**2))/self.GRAVITYSCALE
    
    def acceleration(self,gravity,position,center):
        if (position[0]-center[0]) == 0: angle = 0
        else: angle = math.atan((position[1]-center[1])/(position[0]-center[0]))
        x = gravity*math.cos(angle)
        y = gravity*math.sin(angle)
        if position[0] <= center[0]:
            return [x,y]
        else:
            return [-x,-y]

    def vector(self,bodies,target):
        accelerations = [0,0]
        for body in bodies.values():
            if target == body:
                continue
            grav = self.gravity(Body.distance(target,body)*self.SCALE,body.mass)
            accel = self.acceleration(grav,target.getPosition(),body.getPosition())
            accelerations[0] += accel[0]*self.STEPS
            accelerations[1] += accel[1]*self.STEPS
        return accelerations
    
    def masstodiameter(earthmass):
        # mass in 10**24 kg
        mass = earthmass * 5.9722
        if earthmass < 3:
            rockey = 0.5
        else:
            rockey = 2

        power = 0.325
        constant = 13.8
        diameter = constant * mass**power * rockey
        return diameter