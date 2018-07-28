import cv2
import numpy as np

img = cv2.imread("H:/Github/OpenCv/Research/images/opencv.jpg")


# cv2.imshow("Original",img )


grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(grey,75,127)

ret,thresh = cv2.threshold(edges,70,255,0)
thresh = cv2.subtract(255, thresh) 

# edges = cv2.Canny(thresh,0,255)

cv2.imshow("output",thresh )

cv2.imwrite('output'  + '.jpg' ,thresh )

# kernel = np.ones((2,2),np.uint8)
# dilation = cv2.dilate(thresh,kernel,iterations = 2)
# cv2.imshow("output",dilation )
# cv2.imwrite('output'  + '.jpg' ,dilation )

cv2.waitKey(0)
cv2.destroyAllWindows()