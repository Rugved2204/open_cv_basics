import cv2 as cv
import numpy as np
img1 = cv.imread('Camp.jpg')

img = cv.resize(img1,(400,400),interpolation=cv.INTER_LINEAR)
cv.imshow("Resized",img)


gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#Laplacian calculates the gradient of the grayscale image
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian',lap)

#Sobel
sobelx = cv.Sobel(gray,cv.CV_64F,1,0)
sobely = cv.Sobel(gray,cv.CV_64F,0,1)
combined_sobel = cv.bitwise_or(sobelx,sobely)

cv.imshow('Sobelx',sobelx)
cv.imshow('Sobely',sobely)
cv.imshow('Sobel Combine',combined_sobel)


canny = cv.Canny(gray,150,175)
cv.imshow('Canny',canny)



cv.waitKey(0)