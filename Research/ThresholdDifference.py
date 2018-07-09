import cv2



white = cv2.imread("H:/Github/OpenCv/Research/images/whiteRing.jpg")

black  = cv2.imread("H:/Github/OpenCv/Research/images/black.jpg")
black0 =  cv2.imread("H:/Github/OpenCv/Research/images/black0.jpg")
black1 =  cv2.imread("H:/Github/OpenCv/Research/images/black1.jpg")
black2 =  cv2.imread("H:/Github/OpenCv/Research/images/black2.jpg")

diff = cv2.absdiff(black,black)
print(diff.sum())


diff0 = cv2.absdiff(black,black0)
print(diff0.sum())


diff1 = cv2.absdiff(black,black1)
print(diff1.sum())


diff2 = cv2.absdiff(black,black2)
print(diff2.sum())

print(white)

cv2.waitKey(0)
cv2.destroyAllWindows()