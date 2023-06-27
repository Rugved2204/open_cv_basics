import cv2 as cv
from cv2 import imread
import numpy as np

img = imread('cat.jpg')
cv.imshow('Image',img)

#Transaltion
def translate(img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)

transalted = translate(img,100,100)
cv.imshow('Translated',transalted)


#Rotation
def rotate(img,angle,rotPoint = None):
    (heigth,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,heigth//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimension = (width,heigth)


    return cv.warpAffine(img, rotMat, dimension)

rotated = rotate(img,30)
cv.imshow('Rotated',rotated)

#flipping
flip = cv.flip(img,0)
cv.imshow('Flipped',flip)

cv.waitKey(0)