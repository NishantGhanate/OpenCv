import cv2
import numpy as np

# read as <class 'numpy.ndarray'>
img = cv2.imread("H:/Github/OpenCv/Research/images/red1.jpg")
img1 = cv2.imread("H:/Github/OpenCv/Research/images/blue1.jpg")

# # dst = α ⋅ img1 + β ⋅ img2 + γ

img = cv2.addWeighted(img,0.5,img1,0.3,1)
cv2.imshow("Covert",img )

cv2.waitKey(0)
cv2.destroyAllWindows()
