from random import random, seed
from random import randint
import socketio
import requests
from time import sleep

class drone:

    def __init__(self, DNAME, URL):
        self.dname = DNAME
        self.url = URL
        seed(1)
        return
    
    def connect(self):
        registration = requests.post(self.url + "/drones/" + str(self.dname))
        self.sock = socketio.Client(logger=False, engineio_logger=False)
        self.sock.connect(self.url, socketio_path="/ws/socket.io/") 
    
    def disconnect(self):
        deregistration = requests.post(self.url + "/removedrone/" + str(self.dname))
        self.sock.disconnect()
        return

    def senddata(self, frame):

        # Changing the seed to get random values
        seed(randint(0,1000000))

        # Creating a new payload to send and setting the droneID
        payload = {}
        payload["dname"] = self.dname
        payload["temp"] = self.getTemp()
        payload["pressure"] = self.getPressure()
        payload["humidity"] = self.getHumidity()
        payload["lux"] = self.getLux()
        payload["geiger"] = self.getGeiger()
        payload["gas"] = self.getGas()
        payload["air"] = self.getAir()
        payload["gps"] = self.getGPS()
        payload["cam"] = frame
        payload["tcam"] = frame

        try:
            self.sock.emit("getdata", payload)
        except:
            print("error sending payload")

        return
    
    def getTemp(self):
        return round(randint(-10,100) + random(), 2)
        
    
    def getPressure(self):
        return round(randint(900,1500) + random(), 2)

    def getHumidity(self):
        return round(randint(0,100) + random(), 2)
        

    def getLux(self):
        return round(randint(0,100) + random(), 2)
        
    
    def getGas(self):
        gas = {}

        gas["co"] = round(random(),2)
        gas["no2"] = round(random(),2)
        gas["nh3"] = round(random(),2)
        
        return gas
    
    def getAir(self):
        
        # Creating the Air data structure inside the payload
        air = {}
        
        # Generating random 2dp numbers
        air["pm1"] = round(random(),2)
        air["pm2_5"] = round(random(),2)
        air["pm10"] = round(random(),2)
        
        # Returning
        return air

    def getGeiger(self):
        return randint(0,2500)
        
    
    def getGPS(self):
        gps = {}

        gps["lat"] = round(random(),5)
        gps["long"] = round(random(),5)
        
        return gps


'''    
d1 = drone(0, "http://localhost")

d1.connect()

for i in range(10):
    d1.senddata("he")
    sleep(1)

d1.disconnect()
'''