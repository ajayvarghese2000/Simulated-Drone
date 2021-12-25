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

import tkinter
from typing import Text
import webcam
import PIL.Image, PIL.ImageTk

CAMID = 2
CAM_HEIGHT = 360
CAM_WIDTH = 640

class GUI:
	def __init__(self, window_title):
		self.window = tkinter.Tk()
		self.window.title(window_title)
		self.window.geometry("642x415")
		self.camsource = webcam.camera(CAMID,CAM_WIDTH,CAM_HEIGHT,60)

		self.b1 = tkinter.Button(self.window, text = "Connect to Server")
		self.b2 = tkinter.Button(self.window, text = "Start Data Transfer")
		self.b1.grid(row = 0, column = 0 , sticky=tkinter.W)
		self.b2.grid(row = 1, column = 0 , sticky=tkinter.W)

		self.status = tkinter.Entry(self.window, width=88)
		self.status.grid(column=1, row=1, sticky=tkinter.W)
		self.updatemessage("Server Unconnected")

		self.label = tkinter.Label(self.window, text="Status:")
		self.label.grid(row=0,column=1,sticky=tkinter.W)

		self.canvas = tkinter.Canvas(self.window, width = self.camsource.width, height = self.camsource.height)
		self.canvas.grid(row = 2, column = 0, sticky = tkinter.NW, columnspan = 320)
		

		self.delay = 16
		self.update()

		self.window.resizable(False, False) 
		self.window.mainloop()
	def updatemessage(self,message):
		self.status["state"] = "normal"
		self.status.insert(0,message)
		self.status["state"] = "readonly"
	
	def update(self):
		frame = self.camsource.getFrame()
		self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
		self.canvas.create_image(0, 0, image = self.photo, anchor = tkinter.NW)
		self.window.after(self.delay, self.update)

GUI("Drone-Sim")