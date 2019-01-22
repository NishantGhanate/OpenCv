import numpy as np
import cv2
import os 


scriptDir = os.path.dirname(os.path.realpath(__file__))
fullbody = scriptDir + os.path.sep + "haarcascade_fullbody.xml"

#load cascade xml file itno classifier 
fullbody_cascade = cv2.CascadeClassifier(fullbody)

color = (255,200,0)
cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    bodies =  fullbody_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in bodies:
        cv2.rectangle(img,(x,y),(x+w,y+h),color,2)
    
    cv2.imshow('img',img)
    if cv2.waitKey(30) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()