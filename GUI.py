# A class to create and display the GUI that allows connection to the server
# and display's the webcam feed

## [imports]
import tkinter  # Used to draw the GUI accross systems
import webcam   # Used to access the webcam

# Main Class
#   Functions:
#     Constructor   - Sets up up the GUI and starts to draw it
#     update        - Allows for updating of the webcam feed
#     updatemessage - Allows to update the status box and make it uneditable
class GUI:

    # Constructor class, sets GUI up
    #   Takes in, the name of the GUI, the parameters of the cam, and a drone name
	def __init__(self, window_title, CAMID, CAM_HEIGHT, CAM_WIDTH, CAM_FPS, DNAME):

        # Initialises the tkinter window
		self.window = tkinter.Tk()

        # Giving the Window a name
		self.window.title(window_title)

        # Setting the Window size
		self.window.geometry("642x415")

        # Getting the webcam feed
		self.camsource = webcam.camera(CAMID,CAM_WIDTH,CAM_HEIGHT,CAM_FPS)

        # Creating 2 buttons to connect to server and start data transfer
		self.b1 = tkinter.Button(self.window, text = "Connect to Server")
		self.b2 = tkinter.Button(self.window, text = "Start Data Transfer")
		self.b1.grid(row = 0, column = 0 , sticky=tkinter.W)
		self.b2.grid(row = 1, column = 0 , sticky=tkinter.W)

        # Creating a simple entry field to pass debug information along
		self.status = tkinter.Entry(self.window, width=88)
		self.status.grid(column=1, row=1, sticky=tkinter.W)

        # Setting the start debug message 
		self.updatemessage("Server Unconnected")

        # Creating a simple status label to know if it connected to the server
		self.label = tkinter.Label(self.window, text="Status:")
		self.label.grid(row=0,column=1,sticky=tkinter.W)
        
        # Creating the Canvas that will hold the webcam feed
		self.canvas = tkinter.Canvas(self.window, width = self.camsource.width, height = self.camsource.height)
		self.canvas.grid(row = 2, column = 0, sticky = tkinter.NW, columnspan = 320)

        # The delay for how often the webcam feed updates
		self.delay = 20 # For a 60 FPS cam 10ms is a good delay
        
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
		self.status.insert(0,message)

        # Returns it back to readonly so the user can't change it
		self.status["state"] = "readonly"
	
    # Allows to update the canvas with the webcam feed with the latest frame
	def update(self):

        # Gets the latest frame from the cam
		frame = self.camsource.getFrame()

        # Takes the frame and sets it as the picture
		self.photo = tkinter.PhotoImage(data=frame)

        # Adds the new frame to the canvas
		self.canvas.create_image(0, 0, image = self.photo, anchor = tkinter.NW)

        # Loops through at the given delay on a seprate thread
		self.window.after(self.delay, self.update)
