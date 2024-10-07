#Contours are defiined as the line joining all the points at boundary of an image that are having the same intensity. Contours come in handy in the analysis of shapes, finding the size of the object of intrest, object detection.

import cv2 as cv

img = cv.imread('Phoots/cats.jpg')

cv.imshow('Cats', img)


cv.waitKey(0)