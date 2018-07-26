import cv2
import numpy as np

# read as <class 'numpy.ndarray'>
img = cv2.imread("H:/Github/OpenCv/Research/images/black.jpg")
img1 = cv2.imread("H:/Github/OpenCv/Research/images/fullwhite.jpg")

# cv2.imshow("Original",img )
# cv2.imshow("Original1",img1 )

r,g,b = cv2.split(img)       # get r,g,b
r1,g1,b1 = cv2.split(img1) 

# print(r)
# print(r1)

# # # Check red channel
# if (r.all() > r1.all()):
#     r = r - r1
#     # print(r)
# else:
#     r = r1-r
#     # print("blah as")

# # # Check green channel
# if (g.all() > g1.all()):
#     g = g - g1
#     # print(g)
# else:
#     g = g1-g
#     # print(g)

# # # Check blue channel
# if (b.all() > b1.all()):
#     b = b - b1
#     # print(b)
# else:
#     b = b1-b
#     # print(b)


# Since we get scalar matrix we have to use astype instead of int()

# r = r /2
# r = r.astype(int)
print(r.size)
print(r.shape)

# g = g/2
# g = g.astype(int)
# print(g)

# b = b/2
# b = b.astype(int)
# print(b)

print(r)
img = cv2.merge([r,g1,b1])     # switch it to rgb
cv2.imshow("Covert",img )

cv2.waitKey(0)
cv2.destroyAllWindows()