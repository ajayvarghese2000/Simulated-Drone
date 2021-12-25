# Code to get the webcam feed (simulating the AI object detection camera)

## [Imports]

import cv2 # Used to get the webcam feed

class camera:
    
    def getFrame(self):
        # reads another frame
        success, frame = self.cam.read()

        # checks if we successfully got a frame
        if not success:
            raise IOError("Can not get Frame") 
        else:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            #cv2.imshow('Input', frame)
            #cv2.waitKey(1)
            return frame
    
    def __init__(self,camID, width,height,fps):
        self.cam = cv2.VideoCapture(camID,cv2.CAP_DSHOW)
        self.width = width
        self.height = width
        self.fps = fps
        
        if not self.cam.isOpened():
            raise IOError("Can not open webcam") 

        self.cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        self.cam.set(cv2.CAP_PROP_FPS, fps)

    def __del__(self):
        self.cam.release()
        cv2.destroyAllWindows()

'''cam = camera(2,1920,1080,60)
while True:
    cam.getFrame()'''
