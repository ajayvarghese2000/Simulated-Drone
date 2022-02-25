from random import random, seed, randint    # Used to generate random data values

class GPS:
    def __init__(self):
        self.MAXLONG = -1.187
        self.MINLONG = -1.265
        self.MAXLAT= 52.779
        self.MINLAT = 52.761
        self.LAT = 52.77
        self.LONG = -1.226
        self.LAT_SCALER = 0.0011
        self.LONG_SCALER = 0.00055
        return

    def getPos(self):
        self.genLAT()
        self.genLONG()
        # print(self.LAT, " ", self.LONG)
        return self.LAT, self.LONG
    
    def genLAT(self):

        # 0 is down and 1 is up on a map
        direction = randint(0,1)

        if(direction == 1):

            # Create a random movement
            self.LAT = self.LAT + (random()*self.LAT_SCALER)

            # Check if we've gone past the max
            if (self.LAT >= self.MAXLAT):
                self.LAT = self.MAXLAT
        
            return
        
        self.LAT = self.LAT - (random()*self.LAT_SCALER)

        # Check if we've gone past the max
        if (self.LAT <= self.MINLAT):
            self.LAT = self.MAXLAT
    
        return
    
    def genLONG(self):
        
        # 0 is left and 1 is right on a map
        direction = randint(0,1)

        if(direction == 1):

            # Create a random movement
            self.LONG = self.LONG + (random()*self.LONG_SCALER)

            # Check if we've gone past the max
            if (self.LONG >= self.MAXLONG):
                self.LONG = self.MAXLONG
        
            return

        # Create a random movement
        self.LONG = self.LONG - (random()*self.LONG_SCALER)

        # Check if we've gone past the max
        if (self.LONG <= self.MINLONG):
            self.LONG = self.MINLONG
    
        return
