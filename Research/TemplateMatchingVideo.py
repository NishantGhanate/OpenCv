import cv2
import numpy as np 

cap = cv2.VideoCapture(0)
template = cv2.imread('H:/Github/OpenCv/Research/images/capTemplate1.jpg',cv2.IMREAD_GRAYSCALE)
w, h = template.shape[::-1]

while True:
    _ ,frame = cap.read()
    gray_frame  = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(gray_frame,template,cv2.TM_CCOEFF_NORMED )
    loc = np.where(res >= 0.8)
    for pt in zip(*loc[::-1]):
         cv2.rectangle(frame, pt, (pt[0] + w, pt[1] + h), (0,200,255), 3)

    cv2.imshow("Frame" , frame)
    if cv2.waitKey(27) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()