#OpenCV is a computer vision lib available in Python, C++, Java. CV is an application of deep learning which primarily focuses on driving insights from media files, that is images and videos.

import cv2 as cv

#Now this method basically taken path for the img and then returns the img as a matrix of pixels
img = cv.imread('Images/cat.jpg')

#Now as we have read the image we can show it using cv.imshow() in a new window so the two params we need to pass are the 1.name of the window, 2.actual matrix of pixels to display    
cv.imshow('Cat', img)

#Reading Videos
#The capture var is the instance of the VideoCapture class
capture = cv.VideoCapture('Videos/dog.mp4') #This takes in args such as 1, 2, 3 etc or the path to the video.
#Now to read the video we will run the loop to read the video frame by frame.
while True:
    isTrue, frame = capture.read()
    #As the frames are read the 'frame' var reads the frame and returns the frame and 'isTrue' checks if the frame was sucessfully read.
    cv.imshow('Video', frame) #The imshow() func takes in two params 1.name of the frame, 2.image collected at an instance in the var(frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
    #The waitkey takes in ard as time in millisec and the otehr one states that break the loop until "d" is pressed.

capture.release()
cv.destroyAllWindows()

#After the video completes an error is popped which states error 215: Assertion Failed whic occurs in case if the capture doesnot read any more frames, this can also occur if wrong path is specified'.

#cv.waitKey(0) # Thsi is a keyboard binding func, it basically waiths for he specific time for the keyboard to be pressed, so if u pass 0 then it waits infinitely until any key is pressed.

#There can be some cases wherein u have to resize or rescale images as sometimes the dimentions of the images is greater than the dimention of the monitor 