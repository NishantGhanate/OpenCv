import cv2



white = cv2.imread("H:/Github/OpenCv/Research/images/whiteRing.jpg")
fullwhite = cv2.imread("H:/Github/OpenCv/Research/images/fullwhite.jpg")
hello = cv2.imread("H:/Github/OpenCv/Research/images/helloworld.jpg")
black = cv2.imread("H:/Github/OpenCv/Research/images/black.jpg")
blackball = cv2.imread("H:/Github/OpenCv/Research/images/blackball.jpg")

diff1 = cv2.absdiff(black,white)
print(diff1.sum())

diff2 = cv2.absdiff(hello,fullwhite)
print(diff2.sum())

diff3 = cv2.absdiff(blackball,fullwhite)
print(diff3.sum())

cv2.waitKey(0)

cv2.destroyAllWindows()