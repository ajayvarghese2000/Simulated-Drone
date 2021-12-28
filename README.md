<p align="center">
	<img src="https://i.imgur.com/VwT4NrJ.png">
	<p align="center"> This repository is part of  a collection for the 21WSD001 Team Project. 
	All other repositories can be access below using the buttons</p>
</p>

<p align="center">
	<a href="https://github.com/lboroWMEME-TeamProject/CCC-ProjectDocs"><img src="https://i.imgur.com/rBaZyub.png" alt="drawing" height = 42/></a> 
	<a href="https://github.com/ajayvarghese2000/Dashboard"><img src="https://i.imgur.com/fz7rgd9.png" alt="drawing" height = 42/></a> 
	<a href="https://github.com/ajayvarghese2000/Cloud-Server"><img src="https://i.imgur.com/bsimXcV.png" alt="drawing" height = 42/></a> 
	<a><img src="https://i.imgur.com/yKFokIL.png" alt="drawing" height = 42/></a> 
	<a href="https://github.com/ajayvarghese2000/Simulated-Drone"><img src="https://i.imgur.com/WMOZbrf.png" alt="drawing" height = 42/></a>
</p>

------------

# Simulated Drone
This program simulates the final drone that the team plans to build. It is used to test the server, the communication protocols and, the dashboard that will display the data; without the need of the physical system.

<p align="center">
	<img src="https://user-images.githubusercontent.com/58085441/147592966-a34ca00c-efd3-440f-91ae-e7551c80b545.png"/>
</p>

------------

## Table of Contents

- [Installation](#Installation)
- [Getting Started](#Getting-Started)

------------

## Installation
First clone the repository to a directory on your system.
```
git clone https://github.com/ajayvarghese2000/Simulated-Drone
```
This program is written in python 3, if you don't have it installed download it from the [python website](https://www.python.org/downloads/).
Once python is installed open up a terminal in the directory you cloned the repository and install the dependencies required using pip.

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
```
The ones that will most likely need changing is the `CAMID`, `URL` and the `D_NAME`.

`CAMID` is the ID of the webcam you have plugged in, it is normally 0.

`URL` is the URL of the server to send data to, refer to the [Cloud Server](https://github.com/ajayvarghese2000/Cloud-Serve) documentation to learn how to deploy one.

`D_NAME` is the name of the drone that will be registered with the server.

Once you have defined those variables, you are good to run the script. It should open up a window like the one pictured above.

Hit the button to connect to the server then you will be able to send data.

If the camera you see is not the one you expect, just close the window and change the `CAMID` variable.

------------

## Payload Schema