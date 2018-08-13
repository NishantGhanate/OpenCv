import cv2 
import numpy as np
from matplotlib import pyplot as plt
from playsound import playsound

# playsound('H:/Github/OpenCv/Research/videos/cap.mp3')

img_rgb = cv2.imread('H:/Github/OpenCv/Research/images/cap.jpg')
img_gray =  cv2.cvtColor(img_rgb,cv2.COLOR_BGR2GRAY)
template = cv2.imread('H:/Github/OpenCv/Research/images/capTemplate1.jpg',0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where(res >= threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,200,255), 3)


cv2.imshow("detected",  img_rgb)
cv2.imshow("template ",  template)

cv2.waitKey(0)
cv2.destroyAllWindows()