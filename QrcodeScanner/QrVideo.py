import cv2
import numpy as np
import sys
import time


# Display barcode and QR code location
def display(im, bbox):
    n = len(bbox)
    for j in range(n):
        cv2.line(im, tuple(bbox[j][0]), tuple(bbox[ (j+1) % n][0]), (255,0,0), 3)
    # Display results
    cv2.imshow("Results", im)

cap = cv2.VideoCapture(0)

# Create a qrCodeDetector Object
qrDecoder = cv2.QRCodeDetector()

while True:
    ret , inputImage = cap.read()
    # cv2.imshow(' frame ' , inputImage)
    # Detect and decode the qrcode
    t = time.time()
    data,bbox,rectifiedImage = qrDecoder.detectAndDecode(inputImage)
    print("Time Taken for Detect and Decode : {:.3f} seconds".format(time.time() - t))
    if len(data)>0:
        print("Decoded Data : {}".format(data))
        display(inputImage, bbox)
        rectifiedImage = np.uint8(rectifiedImage)
        cv2.imshow("Rectified QRCode", rectifiedImage)
    else:
        print("QR Code not detected")
        cv2.imshow("Results", inputImage)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

    if cv2.waitKey(1) & 0xFF == ord ( 'q'):
        break

# cv2.imwrite("output.jpg",inputImage)
cv2.waitKey(0)
cv2.destroyAllWindows()

