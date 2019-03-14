import cv2

cap = cv2.VideoCapture(0)
# cap.set(cv2.CV_CAP_PROP_FPS, 10)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)

while True:
    ret , inputImage = cap.read()   
    cv2.imshow(' frame ' , inputImage)
    if cv2.waitKey(1) & 0xFF == ord ( 'q'):
        break

# cv2.imwrite("output.jpg",inputImage)
cv2.waitKey(0)
cv2.destroyAllWindows()