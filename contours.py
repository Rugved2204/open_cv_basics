import cv2 as cv
import numpy as np

img = cv.imread('cat.jpg')
blank = np.zeros(img.shape, dtype = 'uint8')

cv.imshow('Blank',blank)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

blur = cv.GaussianBlur(gray,(3,3),cv.BORDER_DEFAULT)
#canny finds the edges
canny = cv.Canny(blur,125,175)
cv.imshow('Canny',canny)

ret, thresh = cv.threshold(gray,125, 255,cv.THRESH_BINARY)
cv.imshow('Thresh',thresh)

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)

print(len(contours))

cv.drawContours(blank, contours, -1, (0,0,255),1)
cv.imshow('Blanked',blank)


cv.waitKey(0)