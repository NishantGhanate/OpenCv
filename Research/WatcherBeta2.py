import numpy as np
import cv2
from datetime import datetime
import time

timeInterval1 = datetime.now()

def ImageDifference(pastFrame,presentFrame):
    diff = cv2.absdiff(pastFrame,presentFrame)
    # print(diff.sum())
    return diff.sum()
  
cap = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2()
kernel = np.ones((3,3),np.uint8)
kernelSmooth = np.ones( (25,25),np.float32 ) / 625

ret , frame = cap.read()
pastFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
presentFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

pixelDifference = 125000
timeCheck = datetime.now().strftime('%Ss')
ret = True
while(ret):
    ret, img = cap.read()
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    smoothed = cv2.filter2D(imgray,-1,kernelSmooth)
    fgmask = fgbg.apply(smoothed)

    dilation = cv2.dilate(fgmask,kernel,iterations = 2)
    erosion = cv2.erode(dilation,kernel,iterations = 5)

    ret,thresh = cv2.threshold(erosion,127,255,0)
    im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cnt = contours

    # cv2.drawContours(img, contours, -1, (255,0,0), 3)
    for c in contours:
        # print(c)
        rect = cv2.minAreaRect(c)
        # print(rect)
        box = cv2.boxPoints(rect) 
        box = np.int0(box)
        # print(box)
        # print(box)
        cv2.drawContours(img,[box],0,(0,0,255),2)
        cv2.drawContours(erosion,[box],0,(255,255,255),2)

        (x,y),radius = cv2.minEnclosingCircle(c)
        # print(c)
        # print(x,y)
        # print(radius)
        center = (int(x),int(y))
        radius = int(radius)
        cv2.circle(img,center,radius,(0,255,0),2)

    
    if ImageDifference(pastFrame=pastFrame,presentFrame=presentFrame) > pixelDifference and timeCheck !=  datetime.now().strftime('%Ss')  :
        cv2.imwrite(datetime.now().strftime('%Y%m%d %Hh%Mm%Ss%f')  + '.jpg' , img)
       
        # print(timeInterval)
        
    timeCheck = datetime.now().strftime('%Ss')    
    pastFrame , presentFrame  = presentFrame , erosion
     
    # cv2.imshow('Original ',img)
    # cv2.imshow('Background Subtractor ',fgmask)
    cv2.imshow('Erosion',erosion)
    
    if cv2.waitKey(27) & 0xFF == ord('q'):
        break
   

          
cap.release()
cv2.destroyAllWindows()