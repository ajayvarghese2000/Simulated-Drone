#
#  _____ _                 _       _           _       ______                      
# /  ___(_)               | |     | |         | |      |  _  \                     
# \ `--. _ _ __ ___  _   _| | __ _| |_ ___  __| |______| | | |_ __ ___  _ __   ___ 
#  `--. \ | '_ ` _ \| | | | |/ _` | __/ _ \/ _` |______| | | | '__/ _ \| '_ \ / _ \
# /\__/ / | | | | | | |_| | | (_| | ||  __/ (_| |      | |/ /| | | (_) | | | |  __/
# \____/|_|_| |_| |_|\__,_|_|\__,_|\__\___|\__,_|      |___/ |_|  \___/|_| |_|\___|
#
#
# This program is used to simulate the final drones communications to the cloud server
# Will be used to test the servers endpoints and the GUI's representation of data without
# the need of the physicall drone built

## [Imports]
from GUI import GUI				# Used for making the GUI instance
from threading import Thread	# Used to multithread the GUI instances

## [Instance Variables]
CAMID = 2 			# The Cam ID, usually 0, but if you have many cams attached it may change
CAM_HEIGHT = 360	# The height of the camera frame, higher you go, slower preformace (don't change unless needed)
CAM_WIDTH = 640		# The width of the camera frame, higher you go, slower preformace (don't change unless needed)
CAM_FPS = 60		# The FPS of the camera frame, higher you go, slower preformace (don't change unless needed)
D_NAME = "0"		# The drone name that will be registered on the server, keep it simple

# Creating a new thread to start the GUI on
thread1 = Thread(target=GUI, args=("Drone-Sim", CAMID, CAM_HEIGHT, CAM_WIDTH, CAM_FPS, D_NAME))
thread1.start()

### If you have multiple cameras you can run multiple instances of the GUI
### However, remember to change the CAMID you can not open the same cam twice
