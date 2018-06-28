import cv2
import numpy as np
from datetime import datetime

img = cv2.imread("H:/Github/OpenCv/Research/images/whiteRing.jpg")

kernel = np.ones((5,5),np.uint8)

print(kernel)

# nparray = np.array([90,100,20])
# print(nparray)
# dilation = cv2.dilate(img,kernel,iterations = 1)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
# erosion = cv2.erode(img,kernel,iterations = 1)

dilation = cv2.dilate(img,kernel,iterations = 2)
erosion = cv2.erode(dilation,kernel,iterations = 5)


cv2.imshow('original',img)
cv2.imshow('gradient',gradient)
cv2.imshow('erosion',erosion)

cv2.waitKey(0)
cv2.destroyAllWindows()

