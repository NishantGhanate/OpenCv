# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 13:14:28 2018

@author: Nishant Ghanate
"""

import cv2 
import time

#Use 0 if you have only one web camera c
camera = cv2.VideoCapture(0) 
# camera.set(3,1024)
# camera.set(4,1)

# time.sleep(2)

camera.set(15, -5.0)

#Dialog Winddow name
WindowName = "Movement Indicator" 


ret = True

while (ret):
	#Cauz Tuples  set , ret = retry & frame = succesor 
    ret,frame = camera.read()
	# cv2.putText(frame,datetime.now(),(10,500),font, 4,(255,255,255),2,cv2.LINE_AA)
	#Load the window with windowname and videoFeed
    cv2.imshow(WindowName,frame)
	
	#On key 27 [Esc] terminate the program 
    key = cv2.waitKey(27)
    if key == 27:
        cv2.destroyWindow(WindowName)
        camera.release()
        break



""" 0. CV_CAP_PROP_POS_MSEC Current position of the video file in milliseconds.
1. CV_CAP_PROP_POS_FRAMES 0-based index of the frame to be decoded/captured next.
2. CV_CAP_PROP_POS_AVI_RATIO Relative position of the video file
3. CV_CAP_PROP_FRAME_WIDTH Width of the frames in the video stream.
4. CV_CAP_PROP_FRAME_HEIGHT Height of the frames in the video stream.
5. CV_CAP_PROP_FPS Frame rate.
6. CV_CAP_PROP_FOURCC 4-character code of codec.
7. CV_CAP_PROP_FRAME_COUNT Number of frames in the video file.
8. CV_CAP_PROP_FORMAT Format of the Mat objects returned by retrieve() .
9. CV_CAP_PROP_MODE Backend-specific value indicating the current capture mode.
10. CV_CAP_PROP_BRIGHTNESS Brightness of the image (only for cameras).
11. CV_CAP_PROP_CONTRAST Contrast of the image (only for cameras).
12. CV_CAP_PROP_SATURATION Saturation of the image (only for cameras).
13. CV_CAP_PROP_HUE Hue of the image (only for cameras).
14. CV_CAP_PROP_GAIN Gain of the image (only for cameras).
15. CV_CAP_PROP_EXPOSURE Exposure (only for cameras).
16. CV_CAP_PROP_CONVERT_RGB Boolean flags indicating whether images should be converted to RGB.
17. CV_CAP_PROP_WHITE_BALANCE Currently unsupported
18. CV_CAP_PROP_RECTIFICATION Rectification flag for stereo cameras (note: only supported  by DC1394 v 2.x backend currently) """