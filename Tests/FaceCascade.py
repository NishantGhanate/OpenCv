import numpy as np
import cv2
import os 
#download the cascades 
# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades
#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml

scriptDir = os.path.dirname(os.path.realpath(__file__))
face = scriptDir + os.path.sep + "haarcascade_frontalface_default.xml"
eyes = scriptDir + os.path.sep + "haarcascade_eye.xml"
fullbody = scriptDir + os.path.sep + "haarcascade_fullbody.xml"

#load cascade xml file itno classifier 
fullbody_cascade = cv2.CascadeClassifier(fullbody)
face_cascade = cv2.CascadeClassifier(face)
eye_cascade = cv2.CascadeClassifier(eyes)

color = (255,200,0)
cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    bodies =  fullbody_cascade.detectMultiScale(gray, 1.3, 5)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    #for x,y staring point of face x+w y+h end point  255 being BlueGreenRED code , 2 thickness
    for (x,y,w,h) in bodies:
        cv2.rectangle(img,(x,y),(x+w,y+h),color,2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),color,2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
            
            # detect eyes inside face 
        eyes = eye_cascade.detectMultiScale(roi_gray)
        
        for (ex,ey,ew,eh) in eyes:
            # print(eyes)
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

        # if not eyes[:1]:
        #     print("Eyes not found")
        # else :
        #     

        

    cv2.imshow('img',img)
    if cv2.waitKey(30) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
