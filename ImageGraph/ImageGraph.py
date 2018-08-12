import cv2
import matplotlib.pyplot as plt
import numpy as np


img= cv2.imread("H:/Github/OpenCv/FaceRecognition/TrainingImages/img2.jpg")
# print(img.size)
# print(img.shape)

r,g,b = cv2.split(img)       # get r,g,b

# print(r)
# print(g)
# print(b)

red = r[: , 0]
# print(red)

green = g[: , 0]
# print(len(green))

blue = b[: , 0]
# print(len(blue))

plt.plot(red,color='r')
plt.plot(green,color='g')
plt.plot(blue,color='b')
plt.show()

# plt.title('')
# plt.xlabel('')
# plt.ylabel('')
# plt.show()