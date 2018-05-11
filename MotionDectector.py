#pip install opencv-contrib-python
import numpy as np
import cv2
from datetime import datetime

#CaptureVideo use 0 for default webcamera 
cap = cv2.VideoCapture(0)
windowName = "Motion Capture"
threshold = 81500

def ImageDifference(t0,t1,t2):
    d1 = cv2.absdiff(t2,t1)
    d2 = cv2.absdiff(t1,t0)
    return cv2.bitwise_and(d1,d2)

ret , frame = cap.read()
t_minus = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
t = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
t_plus = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

timeCheck = datetime.now().strftime('%Ss')

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if cv2.countNonZero(ImageDifference(t_minus , t , t_plus)) > threshold and timeCheck !=  datetime.now().strftime('%Ss'):
        dimg = frame
        cv2.imwrite(datetime.now().strftime('%Y%m%d_%Hh%Mm%Ss%f')  + '.jpg' , frame)
    # Our operations on the frame come here
    # Display the resulting frame
    cv2.imshow(windowName,frame)
    timeCheck = datetime.now().strftime('%Ss')
    t_minus = t
    t = t_plus
    t_plus =  cv2.cvtColor(frame ,cv2.COLOR_BGR2GRAY )
    
    #press esc or q on load window to end 
    if cv2.waitKey(27) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
