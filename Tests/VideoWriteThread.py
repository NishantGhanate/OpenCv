import cv2
import threading

def video1(cap):
    while True:
        ret , frame = cap.read()
        out.write(frame)
        cv2.imshow(' frame 1' , frame)

    # if cv2.waitKey(1) & 0xFF == ord ( 'q'):
    #     break
    # cap.release()
    # out.release()
    # cv2.destroyAllWindows()


def video2(cap):
    while True:
        ret , frame = cap.read()
        # out.write(frame)
        cv2.imshow(' frame 2 ' , frame)

    # if cv2.waitKey(1) & 0xFF == ord ( 'q'):
    #     break
    # cap.release()
    # out.release()
    # cv2.destroyAllWindows()
    


if __name__=="__main__":
    cap = cv2.VideoCapture(0)
    out = cv2.VideoWriter('C:/Users/Nishant/Pictures/s1.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 15, ( 640,480) )
    t1 = threading.Thread(target=video1, args=(cap,))
    t2 = threading.Thread(target=video2, args=(cap,))

    t1.start()
    t2.start()
   
    
    