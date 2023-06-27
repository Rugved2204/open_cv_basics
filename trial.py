import cv2 as cv
from cv2 import imread
from cv2 import VideoCapture
from cv2 import imshow
from matplotlib.pyplot import sca
import numpy;

img = imread('Camp.jpg')

cv.imshow('Stadium',img)

width = 300
heigth = 300

dimension = (width,heigth)
resized_image = cv.resize(img,dimension, interpolation=cv.INTER_LINEAR)


cv.imshow('Resized Frame', resized_image)


cv.waitKey(0)

cv.destroyAllWindows()