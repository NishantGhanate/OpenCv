import os 
import cv2

def imageToVideo(self,path=None):
    images = []
    video_name = 'new.avi'
    # for p in os.scandir(path):
    #     images.append(p.path)
    for root, dirs, files in os.walk(path):
        for filename in files:
            # print(filename)
            images.append(filename)

    # # sort using prefix number of images cut rest
    sortedImages = sorted(images, key=lambda x: int(x[:-14]))
    # # print(sortedImages)
    Imagepath = os.path.join(path,images[0])
    print(Imagepath)
    frame = cv2.imread(Imagepath)  
    height, width, layers = frame.shape  
    video = cv2.VideoWriter(video_name, 0, 1, (width, height)) 
    for image in sortedImages:  
        Imagepath = os.path.join(path,image)
        print(Imagepath)
            video.write(cv2.imread(Imagepath))
        video.release()


path = "G:\WebScraping\Facebook\Dump\ScreenShots"
imageToVideo(path)