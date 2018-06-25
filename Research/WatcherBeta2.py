import numpy as np
import cv2

# cap = cv2.VideoCapture('H:/Github/OpenCv/Research/videos/car.mp4')
cap = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2()
kernel = np.ones((3,3),np.uint8)
kernelSmooth = np.ones( (25,25),np.float32 ) / 625

while(1):
    ret, img = cap.read()
 
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    smoothed = cv2.filter2D(imgray,-1,kernelSmooth)
    fgmask = fgbg.apply(smoothed)

    cv2.imshow('Original ',imgray)
    cv2.imshow('Smoothed ',smoothed)
    cv2.imshow('fgmask ',fgmask)
    

    if cv2.waitKey(27) & 0xFF == ord('q'):
        break
   

          
cap.release()
cv2.destroyAllWindows()