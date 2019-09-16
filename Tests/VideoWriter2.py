import cv2
import numpy as np
from multiprocessing import Process


out = cv2.VideoWriter('C:/Users/Nishant/Pictures/s1.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 15, ( 640,480) )
def a(frame): 
    cv2.imshow(' frame 1' , frame) 
          

def b(frame):
   frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
   out.write(frame) 
   cv2.imshow(' frame 2' , frame) 
        
    
if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    while True:
        _ , frame = cap.read()
        a(frame)
        b(frame)
        if cv2.waitKey(1) & 0xFF == ord ( 'q'):
            break

cap.release()
out.release()
cv2.destroyAllWindows()


 