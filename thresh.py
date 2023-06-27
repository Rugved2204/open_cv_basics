import cv2 as cv
import numpy as np

img = cv.imread('Camp.jpg')
cv.imshow('Camp',img)

#Simple thresholding
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)


threshold, thresh = cv.threshold(gray,150,255,cv.THRESH_BINARY)
cv.imshow('Simple threshold',thresh)


threshold, thresh_inv = cv.threshold(gray,150,255,cv.THRESH_BINARY_INV )
cv.imshow('Inverse',thresh_inv)

#Adaptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,13,5)
cv.imshow('Adaptive',adaptive_thresh)
cv.waitKey(0)