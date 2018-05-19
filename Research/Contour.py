import cv2
import numpy as np
import datetime as dt
img = cv2.imread("H:/Github/OpenCv/Research/images/shape.jpg")

imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

# returns defects location array matrix
print(contours[-1])

for c in contours:
    print(c)

cnt = contours[-1]

# cv2.drawContours(img, [cnt], 0, (100,255,120), 3)
# cv2.drawContours(img, contours, 1, (255,105,0), 3)
#-1 all 0 first 
#line joing defects
cv2.drawContours(img, contours, -1, (255,0,0), 3)


# contours recieves defects coordinates in array  [no.defect = no.array]
for c in contours:
    print(c)
    rect = cv2.minAreaRect(c)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    # cv2.drawContours(img,[box],0,(0,0,255),2)
    cv2.drawContours(img,[box],-1,(250,10,180),2)

    (x,y),radius = cv2.minEnclosingCircle(c)
    center = (int(x),int(y))
    radius = int(radius)
    cv2.circle(img,center,radius,(0,255,0),2)

  

# (x,y),radius = cv2.minEnclosingCircle(contours[0])
# center = (int(x),int(y))
# radius = int(radius)
# cv2.circle(img,center,radius,(0,255,0),2)

# (x,y),radius = cv2.minEnclosingCircle(contours[-1])
# center = (int(x),int(y))
# radius = int(radius)
# cv2.circle(img,center,radius,(0,255,0),2)


hull = cv2.convexHull(cnt,returnPoints = False)
defects = cv2.convexityDefects(cnt,hull)

for i in range(defects.shape[0]):
    s,e,f,d = defects[i,0]
    start = tuple(cnt[s][0])
    end = tuple(cnt[e][0])
    far = tuple(cnt[f][0])
    cv2.line(img,start,end,[0,2,255],2)
    cv2.circle(img,far,5,[2,20,255],-1)

day = dt.datetime.now().strftime("%A %d %B %Y")
time = dt.datetime.now().strftime("%I:%M:%S %p")
font = cv2.FONT_HERSHEY_SIMPLEX
#cv2.putText(img,'Occupied',(10,450), font, 0.5,(255,100,50),1,cv2.LINE_AA)
cv2.putText(img,day,(10,470), font, 0.5,(0,0,255),1,cv2.LINE_AA)
cv2.putText(img,time,(10,490), font, 0.5,(0,0,255),1,cv2.LINE_AA)
cv2.imshow("Show",img)
cv2.waitKey()
cv2.destroyAllWindows()