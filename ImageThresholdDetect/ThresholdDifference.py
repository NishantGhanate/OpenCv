import cv2


yellow = cv2.imread("H:/Github/OpenCv/ImageThresholdDetect/images/yellow.jpg")
red = cv2.imread("H:/Github/OpenCv/ImageThresholdDetect/images/red.jpg")
green = cv2.imread("H:/Github/OpenCv/ImageThresholdDetect/images/green.jpg")
threshold = 81500

def ImageDifference(s0,s1,s2):
    difference1 = cv2.absdiff(s2,s1)
    print(difference1)
    difference2 = cv2.absdiff(s1,s0)
    print(difference2)
    return cv2.bitwise_and(difference1,difference2)

And = ImageDifference(yellow,red,green)
print(And)


cv2.waitKey(0)