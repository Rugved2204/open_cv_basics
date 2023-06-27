import cv2 as cv

img = cv.imread('cat.jpg')
cv.imshow('Cat',img)

#averaging

average = cv.blur(img,(7,7))
cv.imshow('Average blur',average)

#Gaussian Blur
gauss = cv.GaussianBlur(img,(7,7),0)
cv.imshow('Gausian Blur',gauss)

#Median Blur
median = cv.medianBlur(img,7)
cv.imshow('Median',median)

#Bilateral Blurring (most effective)
bilateral = cv.bilateralFilter(img,5,15,15)
cv.imshow('Bilateral',bilateral)
cv.waitKey(0)