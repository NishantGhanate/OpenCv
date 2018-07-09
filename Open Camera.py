# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 13:14:28 2018

@author: Nishant Ghanate
"""

import cv2 


#Use 0 if you have only one web camera c
camera = cv2.VideoCapture(0) 
#Dialog Winddow name
WindowName = "Movement Indicator" 


#While True because to see continously 
while True:
	#Cauz Tuples  set , ret = retry & frame = succesor 
    ret,frame = camera.read()
	# cv2.putText(frame,datetime.now(),(10,500),font, 4,(255,255,255),2,cv2.LINE_AA)
	#Load the window with windowname and videoFeed
    cv2.imShow(WindowName,frame)
	
	#On key 27 [Esc] terminate the program 
    key = cv2.waitkey(27)
    if key == 27:
        cv2.destroyWindow(WindowName)
        cap.release()
        break