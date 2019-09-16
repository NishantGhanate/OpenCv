import cv2

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 960)

r, frame = cap.read()
...
print('Resolution: ' + str(frame.shape[0]) + ' x ' + str(frame.shape[1]))

out = cv2.VideoWriter('C:/Users/Nishant/Pictures/s6.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 15, ( 1280,960) )
def set_res(cap, x,y):
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, int(x))
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, int(y))
    return str(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),str(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


res = set_res(cap,1209,1220)
print(res)

while True:
    ret , frame = cap.read()
    out.write(frame)
    cv2.imshow(' frame ' , frame)

    if cv2.waitKey(1) & 0xFF == ord ( 'q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
