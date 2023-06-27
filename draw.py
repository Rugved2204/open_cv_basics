from pickletools import uint8
import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8')
cv.imshow("Blank",blank)
blank[200:300,300:400] = 0,255,0
cv.imshow('Green',blank)

cv.rectangle(blank,(0,0), (250,250),(0,255,0),thickness=cv.FILLED)
cv.imshow('Rectangle',blank)
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),30,(255,0,0),thickness = 2)
cv.imshow('Circle',blank)
print(blank.shape[1])
print(blank.shape[0])
cv.putText(blank,'Hello',(255,255),cv.FONT_HERSHEY_TRIPLEX,3.0,(0,0,255),2)
cv.imshow('Text',blank)
cv.waitKey(0)