import cv2
import numpy as np
from datetime import datetime

cap = cv2.VideoCapture(0)
backgroundSubtracter = cv2.createBackgroundSubtractorMOG2()
kernel = np.ones( (25,25),np.float32 ) / 625
font = cv2.FONT_HERSHEY_SIMPLEX

while(1):

    # Take each frame
    _, frame = cap.read()
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    smoothed = cv2.filter2D(grayFrame,-1,kernel)

    cv2.putText(frame,datetime.now().strftime('%Y-%m-%d %H:%M:%S'),(350,450),font, 0.7,(10,10,10),2,cv2.LINE_AA)
    cv2.imshow(" Original " , frame)
    # cv2.imshow(" Kernel  smoothed" , smoothed)
    # subtractedBackground = backgroundSubtracter.apply(smoothed)
    # cv2.imshow(" Median blur ", subtractedBackground  )

    # frame , 15 = pixel round of value 
    # blur = cv2.GaussianBlur( frame , (25,25) , 0 )
    # cv2.imshow(" Blur " , blur)
    
    
    median = cv2.medianBlur( grayFrame , 15 )
    cv2.imshow(" Median blur ", median )

    
    
    # bilateral = cv2.bilateralFilter( res , 15 , 75 , 15 )
    # cv2.imshow( "bilateral blur " , bilateral )

    # denoised_gray = cv2.fastNlMeansDenoising(grayFrame, None, 9, 13)
    # cv2.imshow(" Blur " , denoised_gray)
    
    if  cv2.waitKey(27) & 0xFF == ord('q'):
        break
    

cv2.destroyAllWindows()
cap.release()
