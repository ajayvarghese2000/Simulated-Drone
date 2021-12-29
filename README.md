<p align="center">
	<a href="https://github.com/lboroWMEME-TeamProject/CCC-ProjectDocs"><img src="https://i.imgur.com/VwT4NrJ.png" width=650></a>
	<p align="center"> This repository is part of  a collection for the 21WSD001 Team Project. 
	All other repositories can be access below using the buttons</p>
</p>

<p align="center">
	<a href="https://github.com/lboroWMEME-TeamProject/CCC-ProjectDocs"><img src="https://i.imgur.com/rBaZyub.png" alt="drawing" height = 33/></a> 
	<a href="https://github.com/ajayvarghese2000/Dashboard"><img src="https://i.imgur.com/fz7rgd9.png" alt="drawing" height = 33/></a> 
	<a href="https://github.com/ajayvarghese2000/Cloud-Server"><img src="https://i.imgur.com/bsimXcV.png" alt="drawing" height = 33/></a> 
	<a><img src="https://i.imgur.com/yKFokIL.png" alt="drawing" height = 33/></a> 
	<a href="https://github.com/ajayvarghese2000/Simulated-Drone"><img src="https://i.imgur.com/WMOZbrf.png" alt="drawing" height = 33/></a>
</p>

------------

# Simulated Drone
This program simulates the final drone that the team plans to build. It is used to test the server, the communication protocols and, the dashboard that will display the data; without the need of the physical system.

<p align="center">
	<img src="https://user-images.githubusercontent.com/58085441/147684635-d3843a5e-3fd5-459b-b2f4-55e78eb80755.png"/>
</p>

------------

## Table of Contents

- [Installation](#Installation)
- [Getting Started](#Getting-Started)
- [Data Transfer](#Data-Transfer)
	- [What is a websocket?](#What-is-a-websocket)
	- [Data Schema](#Data-Schema)
		- [Example data packet](#Example-data-packet)
	- [What are base64 encoded images?](#What-are-base64-encoded-images)

------------

## Installation
First clone the repository to a directory on your system. If you have git installed you can use the following command.
```
git clone https://github.com/ajayvarghese2000/Simulated-Drone.git
```
This program is written in python 3, if you don't have it installed download it from the [python website](https://www.python.org/downloads/).
Once python is installed open up a terminal in the directory you cloned the repository and install the dependencies required using pip. It is recommended to use a python virtual environment to avoid conflicts.

To install all the required dependencies run the following command.

```
pip install -r requirements.txt
```

------------

## Getting Started
The program is opened by running the `main.py` file, however some edits must be made before it works.
Before you start you must have a webcam plugged in and not in use by another program. This webcam will simulate the camera that will be on the actual drone.

First open up `main.py` : you need to change the instance variables

```
## [Instance Variables]
CAMID = 0 			        # The Cam ID, usually 0, but if you have many cams attached it may change
CAM_HEIGHT = 360	            	# The height of the camera frame, higher you go, slower performance (don't change unless needed)
CAM_WIDTH = 640		            	# The width of the camera frame, higher you go, slower performance (don't change unless needed)
CAM_FPS = 30		            	# The FPS of the camera frame, higher you go, slower performance (don't change unless needed)
D_NAME = 0		                # The drone name that will be registered on the server, keep it int
URL = "http://localhost"  		# URL of the host server
WEIGHTS = "detection models/yolov4-tiny.weights"    # Files path to the detection model weights
CFG = "detection models/yolov4-tiny.cfg"            # Files path to the detection model configuration
COCO= "detection models/coco.names"                 # Files path to the COCO name data set
```
The ones that will most likely need changing is the `CAMID`, `URL` and the `D_NAME`.

`CAMID` is the ID of the webcam you have plugged in, it is normally 0.

`URL` is the URL of the server to send data to, refer to the [Cloud Server](https://github.com/ajayvarghese2000/Cloud-Server) documentation to learn how to deploy one.

`D_NAME` is the name of the drone that will be registered with the server.

`WEIGHTS` is the file path to the trained detection weights model

`CFG` is the file path to the configuration file for the weights model

`COCO` is the file path for the coco training names dataset

*This repository comes with both the YOLOv3-Tiny and YOLOv4-Tiny trained models*

Once you have defined those variables, you are good to run the script. It should open up a window like the one pictured above.

Hit the button to connect to the server then you will be able to send data.

**The program may hang whist it attempts a connection to the server, just wait patiently until it connects or times out**

If the camera you see is not the one you expect, just close the window and change the `CAMID` variable.

------------

## Data Transfer
The data is sent to the server via a SocketIO websocket connection. It also has a predefined schema, if the schema is not followed the dashboard will not accept the data.

### What is a websocket?
When sending data between a server and client there are a few options on how that can be done. 

The common way is to continually ping the server using a HTTP request with new data. This is ok for small amounts of data and when you are not interested in a real-time response.

<p align="center">
	<img src="https://user-images.githubusercontent.com/58085441/147609412-9e345cd1-a7ac-4e0e-b510-7f1388b9c068.gif" height=200/>
</p>

However, when it comes to real-time communication, this is a bad choice as it acts like a shot-gun sending data randomly with no regard for when it gets processed or if the server is overwhelmed. This is especially the case when you are sending large amounts of data over a short amount of time.

Furthermore, with HTTP requests there is additional overhead as each request must be handled by the server. 

If you want to send data real-time, a good method is to open a websocket on the server. This acts like a queue the drone can send data continuously to. This eliminates the extra overheads with HTTP request as once the websocket is open not additional handling of the data is done.

Then when the server is ready is can load the queue and process however it wants.
<p align="center">
	<img src="https://user-images.githubusercontent.com/58085441/147597894-db29d4ec-ee9f-4362-91dc-f7d4878dd6e9.gif" height=200/>
</p>

In this case, the data is forwarded to the dashboard where it is displayed to the user. The dashboard is also connected via a websocket to the server, it uses that connection to request data about a particular drone that is connected.

### Data Schema
As mentioned before the data that is sent is in a very specific format. If the data sent is not following the established format it will not be processed correctly.

The data from the drone is sent as a JSON packet. ([What is JSON?](https://www.w3schools.com/whatis/whatis_json.asp))

#### Example data packet:

```
{
	"dname": int, 		# The ID of the drone that is registered on the server
	"temp": float,		# The value of the temperature sensor
	"pressure": float,	# The value of the pressure sensor
	"humidity": float,	# The value of the humidity sensor
	"lux": float,		# The value of the light sensor
	"geiger": int,		# The value of the geiger counter
	"gas": {		# Sub-object to hold the values from the gas sensor
		"co": float,	# The Carbon Monoxide reading from the gas sensor
    		"no2": float,	# The Nitrogen Dioxide reading from the gas sensor
    		"nh3": float	# The Ammonia reading from the gas sensor
  	},
  	"air": {		# Sub-object to hold the values from the particulates sensor
    		"pm1": float,	# The value of PM1 particulates in the air
    		"pm2_5": float,	# The value of PM2.5 particulates in the air
    		"pm10": float	# The value of PM10 particulates in the air
  	},
  	"gps": {		# Sub-object to hold the values from the GPS sensor
    		"lat": float,	# The latitudinal position of the drone
    		"long": float	# The longitudinal position of the drone
  	},
  	"cam": base64,		# The image from the object-detection camera base64 encoded
  	"tcam": base64		# The image from the thermal camera base64 encoded
}
```

Most of the data in the data packet is self-explanatory with exception of the base64 encoded images.

### What are base64 encoded images?
The images that are received from the cameras on the drones will be raw binary data. 

The dashboard needs the newest frame from the drone to display to the user however, if we send the raw binary data in the data packet, it would make the size of the packet very large, hard to read and, longer to parse through.

base64 encoding takes the raw binary data and encodes it in base64, this gives a much smaller string that can be inserted into the data packet. [More on base64](https://en.wikipedia.org/wiki/Base64)

The best way to send the camera feeds would be to encode a video on the drone of the last few seconds then upload that chuck to the server just like how YouTube and Twitch work. This way, you can take advantage of modern video compression algorithms to make the data as small as possible.

However that would not be good for this use case as:

1. The hardware the drone firmware is deployed on is not very powerful. Having to encode a video as well as run object-detection and getting values from sensors will overwhelm it.
2. It would increase the latency as the server will have to first wait for the chuck to be encoded, then uploaded.

Base64 does have its disadvantages, namely that it take about 33% more resources to encode and decode when compared to binary data. However, most modern devices will be able to handel that increase without issue.
