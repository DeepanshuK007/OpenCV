import cv2 as cv

img = cv.imread('Photos/cat.jpg')

cv.imshow('Cat', img)

#Converting an img to greyscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#Takes in args such as the source img and the conversion code 
cv.imshow('Gray', gray)

#Blur an image
#Removes some of the exsisting noise in the img such as bad lighting, problems in the camera sensor. We do it by creating a Gaussian img
blur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
#Takes in args such as-> 1.source image, 2. kernel size which is a 2 by 2 tulpe which is the window size that open cv uses to compute the blown image, has to be an odd no, 3.BORDER_DEFAULT 
cv.imshow("Blur", blur)

#To increase the intensity of blurness u can increase the kernel size
#blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)

# Edge Cascade
# Helps us to find the edges of the image, we will be using Canny edge detector
# The args are-> 1.source img, 2.threshold value 1, 3.threshold value 2
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', canny)

#We can reduce the amount of edges by instead of passing the original image we can pass the blured img
#canny = cv.Canny(blur, 125, 175)

#Dilating an Image using edges
# Dilation adds pixels to the boundaries of objects in an img
dilated = cv.dilate(canny, (7, 7), iterations=3)
cv.imshow('Dilated', dilated)
# The dilated image thickens the canny edges and the thickness increases as we increase the iterations.

#Eroding
# Removes pixels on object boundaries
# So if we apply eroding on an dilated image we get the Canny image back 
eroded = cv.erode(dilated, (7, 7), iterations=3)

# Resize
resized = cv.resize(img, (500, 500))
# Takes in -> 1.image to be resized, 2. destination (ignoring the aspect ratio)
''' In this u can also use the interpolation methods such as 
1. INNER_AREA - Useful if u are shrinking the img to the dimentions that are smaller than that of the of the og dimentions.
2. INTER_LINEAR - If u want to enlarge to a larger dimention or INTER_CUBIC. 
3. INTER_CUBIC is the slowest among them all but the result we get of much higher dimention. 
'''
cv.imshow('Resized', resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)