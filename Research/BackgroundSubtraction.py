import numpy as np
import cv2

cap = cv2.VideoCapture('H:/Github/OpenCv/Research/videos/car.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2()
kernel = np.ones((3,3),np.uint8)
kernelSmooth = np.ones( (25,25),np.float32 ) / 625
while(1):
    ret, img = cap.read()
    # img = np.rot90(img)
    # img = np.rot90(img)
    # img = np.rot90(img) 

    grayFrame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    smoothed = cv2.filter2D(grayFrame,-1,kernelSmooth)
    fgmask = fgbg.apply(smoothed)
    dilation = cv2.dilate(fgmask,kernel,iterations = 2)
    erosion = cv2.erode(dilation,kernel,iterations = 2)

    cv2.imshow('Original ',img)
    cv2.imshow('Background Subtractor ',fgmask)
    cv2.imshow('Erosion',erosion)
    
    if cv2.waitKey(27) & 0xFF == ord('q'):
        break
   

          
cap.release()
cv2.destroyAllWindows()