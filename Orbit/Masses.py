from Body import *

class Masses:

    def __init__(self,window,canvas):
        self.window = window
        self.canvas = canvas

    def getNone(self):
        nonemass = 0
        nonepos = [300,300]
        nonevector = [0,0]
        nonediameter = 0
        return Body(self.window,self.canvas,nonemass,nonediameter,nonepos[0],nonepos[1],nonevector[0],nonevector[1],"none","black","none")

    def getSun(self):
        sunmass = 1.988416 * 10**30 
        sunpos = [300,300]
        sunvector = [0,0]
        sundiameter = 1.392
        return Body(self.window,self.canvas,sunmass,sundiameter,sunpos[0],sunpos[1],sunvector[0],sunvector[1],"sun","yellow","sun")
    
    def getMercury(self):
        mercurymass = 3.3010 * 10**23
        mercurypos = [346,300]
        mercuryvector = [0,-58970]
        mercurydiameter = 0.004881
        return Body(self.window,self.canvas,mercurymass,mercurydiameter,mercurypos[0],mercurypos[1],mercuryvector[0],mercuryvector[1],"sun","#CECECE","mercury")    
    
    def getVenus(self):
        venusmass = 4.8673 * 10**24
        venuspos = [192.52,300]
        venusvector = [0,35260]
        venusdiameter = 0.0121036
        return Body(self.window,self.canvas,venusmass,venusdiameter,venuspos[0],venuspos[1],venusvector[0],venusvector[1],"sun","#A78D24","venus")    

    def getEarth(self):
        planetmass = 5.9722 * 10**24
        planetpos = [147.9,300]
        planetvector = [0,29290]
        planetdiameter = 0.012742
        return Body(self.window,self.canvas,planetmass,planetdiameter,planetpos[0],planetpos[1],planetvector[0],planetvector[1],"sun","#5DE9B6","earth")
    
    def getMoon(self):
        moonmass = 7.346 * 10**22
        moonpos = [147.4945,300]
        moonvector = [0,30260]
        moondiameter = 0.003475
        return Body(self.window,self.canvas,moonmass,moondiameter,moonpos[0],moonpos[1],moonvector[0],moonvector[1],"earth","#AFAFAF","moon")

    def getMars(self):
        marsmass = 6.4169 * 10**23
        marspos = [93.35,300]
        marsvector = [0,26500]
        marsdiameter = 0.0067924
        return Body(self.window,self.canvas,marsmass,marsdiameter,marspos[0],marspos[1],marsvector[0],marsvector[1],"sun","#E15B0D","mars")

    def getJupiter(self):
        jupitermass = 1.89813 * 10**27
        jupiterpos = [-440.595,300]
        jupitervector = [0,13720]
        jupiterdiameter = 0.142984
        return Body(self.window,self.canvas,jupitermass,jupiterdiameter,jupiterpos[0],jupiterpos[1],jupitervector[0],jupitervector[1],"sun","#FF9E01","jupiter")    

    def getGanymede(self):
        ganymedemass = 1.4819 * 10**23
        ganymedepos = [-441.6642,300]
        ganymedevector = [0,24600]
        ganymedediameter = 0.0052682
        return Body(self.window,self.canvas,ganymedemass,ganymedediameter,ganymedepos[0],ganymedepos[1],ganymedevector[0],ganymedevector[1],"jupiter","#A9A6A6","ganymede")   
      
    def getEuropa(self):
        europamass = 4.79984 * 10**22
        europapos = [-441.259862,300]
        europavector = [0,27464]
        europadiameter = 0.0031216
        return Body(self.window,self.canvas,europamass,europadiameter,europapos[0],europapos[1],europavector[0],europavector[1],"jupiter","#C9B49C","europa")    
 
    def getSaturn(self):
        saturnmass = 5.6851 * 10**26
        saturnpos = [-1057.554,300]
        saturnvector = [0,10140]
        saturndiameter = 0.120536
        return Body(self.window,self.canvas,saturnmass,saturndiameter,saturnpos[0],saturnpos[1],saturnvector[0],saturnvector[1],"sun","#FFECA1","saturn")    
    
    def getUranus(self):
        uranusmass = 8.6849 * 10**25
        uranuspos = [-2432.696,300]
        uranusvector = [0,7300]
        uranusdiameter = 0.051118
        return Body(self.window,self.canvas,uranusmass,uranusdiameter,uranuspos[0],uranuspos[1],uranusvector[0],uranusvector[1],"sun","#A3F5F8","uranus")   
    
    def getNeptune(self):
        neptunemass = 1.0244 * 10**26
        neptunepos = [-4171.05,300]
        neptunevector = [0,5470]
        neptunediameter = 0.049528
        return Body(self.window,self.canvas,neptunemass,neptunediameter,neptunepos[0],neptunepos[1],neptunevector[0],neptunevector[1],"sun","#1D16B3","neptune")  

    def getTriton(self):
        tritonmass = 2.1389 * 10**22
        tritonpos = [-4171.404759,300]
        tritonvector = [0,9860]
        tritondiameter = 0.0027068
        return Body(self.window,self.canvas,tritonmass,tritondiameter,tritonpos[0],tritonpos[1],tritonvector[0],tritonvector[1],"neptune","#AED3CA","triton")   