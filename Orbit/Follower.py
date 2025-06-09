class Follower:

    def __init__(self,window,canvas,key,body,calc,traildistance):
        self.window = window
        self.canvas = canvas
        self.key = key
        self.body = body
        self.calc = calc
        self.traildistance = traildistance
        self.trail = []
        self.prev = self.body.getPosition()
        self.frequency = 1
        self.animation = 200000000
        self.count = 0
    
    def drawpaths(trails):
        for trail in trails.values():
            trail.drawpath()

    def drawpath(self):
        if self.count%self.frequency == 0:
            coords = self.body.getPosition()
            self.drawline(coords)
            if len(self.trail) > self.traildistance:
                self.canvas.delete(self.trail[0])
                self.trail.pop(0)
            self.prev = coords
            self.count = 0
            self.updatefrequency()
        self.count += 1

    def drawline(self,coords):
        line = self.canvas.create_line(self.prev[0],self.prev[1],coords[0],coords[1],fill="white")
        self.trail.append(line)

    def skip(self):
        self.drawline(self.body.getPosition())
    
    def updateprev(self):
        self.prev = self.body.getPosition()

    def updatefrequency(self):
        if self.body.getVelocity() == 0:
            self.frequency = 100
        else:
            self.frequency = max(1,int(self.animation/(self.body.getVelocity()*self.calc.STEPS)))
