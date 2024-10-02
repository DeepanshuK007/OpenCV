#We usually resize and rescale images to prevent computational strains. Large info files tand to store a lot of info in it, thus to get rid of some of the info, rescaling adjusts/modifies its height and width to a particular value.

import cv2 as cv

img = cv.imread('Photos/cat_large.jpg')
cv.imshow('Cat', img)

#Func if we want to change the resolution of a live video
def changeRes(width, height):
    capture.set(3, width)
    capture.set(4, height)

#Func if we want to adjust the already present video or img or live video
#Declared a func with the params frame and the scale to resize in is 0.75(standard)
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale) # width of img= current * 0.75
    height = int(frame.shape[0] * scale)
    dimentions = (width, height) 

    return cv.resize(frame, dimentions, interpolation=cv.INTER_AREA)

resized_img = rescaleFrame(img)
cv.imshow('Image', resized_img)

'''called the .resize func and passed the args in it with the fame to be resized, the dimentions and the interpolation type.

Interpolation is the process of determining the unknown values lying in between the known data points.

INTER_AREA is a bit complicated type of interpolation as compared to others such as INTER_NEAREST, INTER_LINEAR etc., as it does resampling using pixel area relation.
'''

#Reading Videos
capture = cv.VideoCapture('Videos/dog.mp4') 
while True:
    isTrue, frame = capture.read()
    # frame_resized = rescaleFrame(frame) #Here we use the rescaleFrame func to rescale the frame captured from the above line.
    frame_resized = rescaleFrame(frame, scale=0.2)
    
    cv.imshow('Video', frame) 
    cv.imshow('Video_Resized', frame_resized) 

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
    

cv.waitKey(0)