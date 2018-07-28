import cv2
import numpy as np

img = cv2.imread("H:/Github/OpenCv/Research/images/opencv.jpg")
# cv2.imshow("Original",img )
grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(grey,75,127)
ret,thresh = cv2.threshold(edges,70,255,0)
thresh = cv2.subtract(255, thresh) 

im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for c in contours:
    # cv2.fillPoly(thresh, pts =[c], color=(45,240,100))
    cv2.polylines(thresh,[c],True,(0,255,255),2)
    # print(c)

cv2.imshow("output",thresh )
cv2.imwrite('output'  + '.jpg' ,thresh )

cv2.waitKey(0)
cv2.destroyAllWindows()



# edges = cv2.Canny(thresh,0,255)
# cv2.imshow("output",thresh )
# cv2.imwrite('output'  + '.jpg' ,thresh )
# dst = cv2.inpaint(thresh,img,3,cv2.INPAINT_TELEA)
# kernel = np.ones((2,2),np.uint8)
# dilation = cv2.dilate(thresh,kernel,iterations = 2)
# 
# 