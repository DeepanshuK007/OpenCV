#Drawing Shapes and Putting Texts
import cv2 as cv
import numpy as np

#Either we can work on the image provided or we can work on a dummy/blank image
blank = np.zeros((500, 500, 3), dtype='uint8')
#.zeroes returns a new array will with zeroes, takes param such as 1.size(height, width, no of color channels), 2.dtype...
cv.imshow('Blank', blank)

#1. Paint the img a certain color
blank[:] = 0, 255, 0  #This will color the whole arr of the Blank window green
cv.imshow('Green', blank)

#2. Draw a rectangle
# cv.rectangle(blank, (0,0), (250, 250), (0, 255, 0), thickness=2)
#.rectangle is a func inside cv2 which takes args 1.img, 2.pnt1 coordinates, 3.pnt 2 coords., 4.thickness
#The thickness value is taken as the color is only filled on the border of that thikness of the rectangle, to fill the while rectangle with color use cv.FILLED/ -1

# cv.rectangle(blank, (0,0), (250, 250), (0, 255, 0), thickness=cv.FILLED)

cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0, 255, 0), thickness=cv.FILLED)
#Instead of passing  

cv.imread('Rectangle', blank)

#3. Draw a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=-1)
#.cirle takes in arguments -> 1.the img, 2.the centre coords, 3.the radius in pix, 4.color, 5.thickness
cv.imshow('Circle', blank)

#4. Draw a line
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=3)
#.line takes in arguments -> 1.image, 2.start pt, 3.end pt, 4.color, 5.thickness
cv.imshow('Line', blank)

#5. Write text
cv.putText(blank, 'Hello', (225, 225), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), 2)
#.putText taken in args such as 1.image, 2.Text to write, 3.origin, 4.font_type, 5.text_size, 6.color, 7.thickness
cv.imshow('Text', blank)

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat', img)

cv.waitKey(0)