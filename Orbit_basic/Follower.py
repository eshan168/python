class Follower:

    def __init__(self,window,canvas,key,body,calc,traildistance):
        self.window = window
        self.canvas = canvas
        self.key = key
        self.body = body
        self.calc = calc
        self.traildistance = traildistance
        self.frequency = 8
        self.count = 0

        self.points = self.body.getPosition() + self.body.getPosition()
        self.trail = self.canvas.create_line(self.points,fill="white",width=2,smooth=True)
    
    def drawpaths(trails):
        for trail in trails.values():
            trail.drawpath()

    def drawpath(self):
        if self.count%self.frequency == 0:
            self.points += self.body.getPosition()
            self.drawline(self.points)

            if len(self.points) > self.traildistance:
                self.points = self.points[2:]
            self.count = 0
        self.count += 1

    def drawline(self,points):
        if self.key == "nonetrail":
            return
        self.canvas.coords(self.trail, points)

    def rescale(self, zoomscale, center):
        screen_points = []
        for i in range(0, len(self.points), 2):
            x = (self.points[i]-center[0])*zoomscale + center[0]
            y = (self.points[i+1]-center[1])*zoomscale + center[1]
            screen_points += [x,y]
        self.points = screen_points
        self.canvas.coords(self.trail, self.points)

    def updatefrequency(self):
        if self.body.getVelocity() == 0:
            self.frequency = 100
        else:
            self.frequency = 10
