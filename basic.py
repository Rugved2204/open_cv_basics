import cv2 as cv
import numpy as np


img = cv.imread('cat.jpg')
cv.imshow('Image',img)

#grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#blur removes some of the noise in the image
blur = cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

#edge cascade is use to detect edges
cany = cv.Canny(blur,125, 175)
cv.imshow('Canny',cany)

#Dilating the image
#Dilation is a technique where we expand the image. 
#It adds the number of pixels to the boundaries of objects in an image
dilated = cv.dilate(cany,(8,8), iterations=1)
cv.imshow('Dilated',dilated)

#eroding
eroded = cv.erode(dilated,(3,3),iterations=1)
cv.imshow('Eroded',eroded)

#resize
resize = cv.resize(img,(100,100),interpolation=cv.INTER_LINEAR)
cv.imshow("Resized",resize)

#cropping
cropped = img[50:200,200:400]
cv.imshow('Cropped',cropped)

cv.waitKey(0)