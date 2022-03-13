# A class to create and display the GUI that allows connection to the server
# and display's the webcam feed
#
#   Written by Team CCC
#

## [imports]
from datetime import datetime
import tkinter					# Used to draw the GUI accross systems
import webcam   				# Used to access the webcam
from drone import drone			# Used to generate data from sensors and send info
from PIL import ImageTk
import base64

# Main Class
#   Functions:
#     Constructor   - Sets up up the GUI and starts to draw it
#     update        - Allows for updating of the webcam feed
#     updatemessage - Allows to update the status box and make it uneditable
#	  datatransfer	- Handles the toggling between starting/stopping the data transfer
# 	  connect		- Handles the toggling between connecting/disconnecting the server
#	  on_closing	- Cleans up loose connecting when the window is closed
class GUI:

    # Constructor function, sets GUI up
    #   Takes in, the name of the GUI, the parameters of the cam, and a drone name
	def __init__(self, window_title, CAMID, CAM_HEIGHT, CAM_WIDTH, CAM_FPS, DNAME, URL, WEIGHTS, CFG, COCO):

        # Initialises the tkinter window
		self.window = tkinter.Tk()

        # Giving the Window a name
		self.window.title(window_title)

        # Setting the Window size
		self.window.geometry("642x415")

		# Setting the on_close protocol
		self.window.protocol("WM_DELETE_WINDOW", self.on_closing)

        # Getting the webcam feed
		self.camsource = webcam.camera(CAMID,CAM_WIDTH,CAM_HEIGHT,CAM_FPS, WEIGHTS, CFG, COCO)

		# Creating the Drone element
		self.drone = drone(DNAME, URL)

		# Creating variable to check if we need to connect/disconnect
		self.sending = False

		# Creating variable to check if we need to send data/stop sending
		self.connected = False

        # Creating 2 buttons to connect to server and start data transfer
		self.b1 = tkinter.Button(self.window, text = "Connect to Server", command=self.connect)
		self.b2 = tkinter.Button(self.window, text = "Start Data Transfer", command=self.datatransfer)
		self.b1.grid(row = 0, column = 0 , sticky=tkinter.W)
		self.b2.grid(row = 1, column = 0 , sticky=tkinter.W)

        # Creating a simple entry field to pass debug information along
		self.text = tkinter.StringVar()
		self.status = tkinter.Entry(self.window, width=88, textvariable=self.text)
		self.status.grid(column=1, row=1, sticky=tkinter.W)

        # Setting the start debug message 
		self.updatemessage("Server Unconnected")

        # Creating a simple status label to know if it connected to the server
		self.label = tkinter.Label(self.window, text="Status : Disconnected")
		self.label.grid(row=0,column=1,sticky=tkinter.W)
        
        # Creating the Canvas that will hold the webcam feed
		self.canvas = tkinter.Canvas(self.window, width = self.camsource.width, height = self.camsource.height)
		self.canvas.grid(row = 2, column = 0, sticky = tkinter.NW, columnspan = 320)

        # The delay for how often the webcam feed updates
		self.delay = int(round((1/CAM_FPS) * 1000,0))
        
        # Updating the canvas with the latest frame
		self.update()

        # Making the Window non-resizable 
		self.window.resizable(False, False)

        # starting the tkinter GUI on a separate thread
		self.window.mainloop()
    
    # Allows to update the debug status entry with a custom message
	def updatemessage(self,message):

        # Sets the state to normal so it it editable
		self.status["state"] = "normal"

        # Changes the message
		self.text.set(message)

        # Returns it back to readonly so the user can't change it
		self.status["state"] = "readonly"
	
    # Allows to update the canvas with the webcam feed with the latest frame
	def update(self):

        # Gets the latest frames and person variable from the cam
		self.frame, self.thermal_frame, self.person = self.camsource.getFrame()

        # Takes the frame and sets it as the picture
		self.photo = ImageTk.PhotoImage(data=base64.b64decode(self.frame))

        # Adds the new frame to the canvas
		self.canvas.create_image(0, 0, image = self.photo, anchor = tkinter.NW)

		# Checks if the client is meant to send data
		if self.sending == True:

			# Gets the current time for a timestamped debug message
			current_time = datetime.now().strftime("%H:%M:%S.%f")[:-3]

			# Updates the debug status to let the user know data was sent
			self.updatemessage(current_time + " Sent Data Packet")

			# Insturcts the drone to send data over to the server
			self.drone.senddata(self.frame, self.thermal_frame, self.person)

        # Loops through at the given delay on a seprate thread
		self.window.after(self.delay, self.update)
	
	# Function to handel if the client sends data to the server or not
	def datatransfer(self):

		# Checks if the client is connected to the server
		if self.connected == False:

			# If the client is not connected we return as no data should be sent
			self.updatemessage("Not connected to server")

			# Updates the button to say start again
			self.b2["text"] = "Start Data Transfer"

			return
		
		# Handles the toggle betwen starting and stopping data to be sent
		if self.sending == True:

			# As sending was originals true, the client now turns off sending
			self.sending = False

			# Updates the button to say start again
			self.b2["text"] = "Start Data Transfer"
			return
		
		# If sending was false, we now turn it back on
		self.sending = True

		# Changes the button to say Stop
		self.b2["text"] = "Stop Data Transfer"

		# returning back to the main loop
		return
	
	# Function to handel the connection between the server and the client
	def connect(self):
		
		# Disconnect code
		if self.connected == True:

			# Attempts disconnection, if return is 1 then it was successful
			if self.drone.disconnect() == 1:

				# Updating the button
				self.b1["text"] = "Connect to Server"

				# Updating the connection status
				self.label["text"] = "Status : Disconnected"

				# Updating the debug log
				self.updatemessage("Disconnected from server")

				# Turning sending off
				self.sending = False

				# Updating the connection variable
				self.connected = False

				# Updating the send data button
				self.datatransfer()

				# Exiting function
				return
			
			# If there is a disconnection failure alert user then exit
			self.updatemessage("Failed to disconnect")
			return
		
		# Attempts a connection to server, if return is 1 then it was successful
		if self.drone.connect() == 1:

			# Updates the connection variable
			self.connected = True

			# Updating the connection status
			self.label["text"] = "Status : Connected"

			# Updating the button text
			self.b1["text"] = "Disconnect from Server"

			# Adding a message to the debug log then exiting
			self.updatemessage("Connected to server")
			return
		
		# If there is a issue with connecting, issue a message the return
		self.updatemessage("Failed to connect to server")
		return
	
	# Function to clean up any connections when the user closes the window without
	# Disconnecting from the server
	def on_closing(self):

		# Turn off sending and disable the connected variable
		self.sending = False
		self.connected = False

		# Attempt a disconnect, if it fails print to console
		if self.drone.disconnect() == 0:
			print("error closing connection, was it even active?")
			
		# destroy the tkinter window
		self.window.destroy()
		return
