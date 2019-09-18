import cv2
import base64

img = cv2.imread("D:/21.jpg")


retval, buffer = cv2.imencode('.jpg', img)
jpg_as_text = base64.b64encode(buffer) 
print('len before : ',len(jpg_as_text))
print('Original Dimensions : ',img.shape)
 
scale_percent = 40 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
# resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)


retval, buffer = cv2.imencode('.jpg', resized)
jpg_as_text = base64.b64encode(buffer) 
print('len after : ',len(jpg_as_text))
print('Resized Dimensions : ',resized.shape)
 
with open("D:/21.jpg", "rb") as image:
    f = image.read()
    print( type(f) )
    print( len(f) )
    b = bytearray(f)
    print(type(b))
    print(len(b))
     
 
 
# cv2.imshow("Resized image", resized)
# cv2.waitKey(0)
# cv2.destroyAllWindows()