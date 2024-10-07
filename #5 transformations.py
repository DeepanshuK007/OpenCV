import cv2 as cv
import numpy as np

img = cv.imread('Photos/boston.jpg')

cv.imshow('Boston', img)

# Translations
# Using translations we can shift any img up down left right.
def translate(img, x, y):
    #We create a func in which we take in args-> 1.source img, 2.the x coordinated in which we have to shift the image, 2. the y coordinates

    #To translate an img we need to take an translation matrix 
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    #Takes in two lists inside of it

    dimentions = (img.shape[1], img.shape[0])
    #shape[1] is the width and shape2 is the height

    return cv.warpAffine(img, transMat, dimentions)
    #Takes in args such as the source img, translation matrix and the dimentions of the og img

'''
The wrapAffine transformation in OpenCV applies an affine transformation to an img.
Affine transformations allows us to use simple system of linear equations to manipulate any points or set of pts.
'''

#If u enter the values of -x, translates to the left. 
# -y -> Up
# x -> Right
# y -> Down
translate(img, 100, 100) #Here we have shifted the image right by 100 pix and down by 100 pix.

# Rotations 
# OpenCV allows u to rotate the img by some angle. about any rotation pt youd like to rotate the img around.
def rotate (img, angle, rotPoint=None):
    (height, width) = img.shape[:2] #Consider the first two pts of the array

    if rotPoint is None: #Assume we are going to rotate around centre
        rotPoint = (width//2, height//2) #centre points

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    # Takes in args such as 1. rotation pt, 2. angle of rotation, 3.scale val
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions) #Here dimentions represent the third arg that is the destination cords

rotated = rotate(img, -90)
cv.imshow('Rotated', rotated)

#Resizing 
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
#The args are -> 1.source img, 2.destination size (frame scale), 3.interpolation
cv.imshow('Resized', resized)

# Flipping
flip = cv.flip(img, 0)
# The args are -> 1.src img, 2.flip code (0 -> vertical flip, 1 -> horizontal flip, -1 -> both) 
cv.imshow('Flip', flip)

# Cropping 
cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
