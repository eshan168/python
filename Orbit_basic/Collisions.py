from Body import *
from Display import *

class Collisions:
    
    def __init__(self,window,canvas,keys,bodies,trails,display:Display):
        self.window = window
        self.canvas = canvas
        self.keys = keys
        self.bodies = bodies
        self.trails = trails
        self.display = display
        self.zoomscale = 1
    
    def checkcollisions(self,targetbody:Body,bodies:dict):
        for body in bodies.values():
            if body == targetbody or body.key == "none":
                continue
            elif self.collision(targetbody,body):
                break

    def collision(self,body1:Body,body2:Body):
        distance = Body.distance(body1,body2)/self.zoomscale
        min = (body1.radius+body2.radius)
        if distance <= min:
            print(min,distance,body1.key,body2.key)
            return self.collide(body1,body2)
        return False
    
    def collide(self,body1:Body,body2:Body):
        if body1.mass <= body2.mass:
            self.display.deletebody(body1.key)
        else:
            self.display.deletebody(body2.key)
        return True
