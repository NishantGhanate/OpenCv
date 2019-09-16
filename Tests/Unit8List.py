import numpy as np
import cv2



path = "C:/Users/Nishant/Pictures/gta-5-wasted_1.jpg"

# file = open(path, 'rb')
# blob = file.read()
# file.close()

# print(blob)

img= cv2.imread(path)

for i in img:
    print(i)
