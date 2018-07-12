import cv2
import numpy as np
import matplotlib.pyplot as plot
import base64

img = cv2.imread("H:/Github/OpenCv/Research/images/rgb.jpg")

retval, buffer = cv2.imencode('.jpg', img)
jpg_as_text = base64.b64encode(buffer)
print(type(jpg_as_text))

# b,g,r = cv2.split(img)       # get b,g,r
# img = cv2.merge([r,g,b])     # switch it to rgb
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# cv2.imshow("" ,img )

# img = cv2.imencode('.jpg', img)[1].tostring()
# # type(img_str)
# print(img)

# img = cv2.imdecode( np.asarray(bytearray(img), dtype=np.uint8), 1 )
# print(img)

# red=img[:,:,0]
# green=img[:,:,1]
# blue=img[:,:,2]
# print(blue)
# image_convert=np.array([red,green,blue])
# print(image_convert.shape)
# plot.imshow(image_convert[1,:,:])
# plot.show()

# with open("H:/Github/OpenCv/Research/images/rgb.jpg", "rb") as imageFile:
#   f = imageFile.read()
#   b = bytearray(f)

# print (b)

cv2.waitKey(0)
cv2.destroyAllWindows()