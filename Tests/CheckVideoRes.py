import cv2

resolutions = [[480,360] , [640,480] , [720,480] , [800,480] , [800,600] , [960,720] , [1024,768], [1280,720], [1280,800 ], [1280,960] ,[1280,1024] ,[1600,1200] ,[1920,1080] ]

out = cv2.VideoWriter('C:/Users/Nishant/Pictures/s6.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 24, ( 1280,960) )

def setResolution(cap, x):
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, x[0])
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT,x[1] )
    r, frame = cap.read()
    # print('Resolution: ' + str(frame.shape[0]) + ' x ' + str(frame.shape[1]))
    return [ int ( cap.get(cv2.CAP_PROP_FRAME_WIDTH) ), int ( cap.get(cv2.CAP_PROP_FRAME_HEIGHT) ) ]

def part(n):
    cap = cv2.VideoCapture(0)
    for r in resolutions: 
        print(setResolution(cap,r))
            
        
            
part(1)  



 
    
# res = set_res(cap,1209,1220)
# print(res)

# while True:
#     ret , frame = cap.read()
#     out.write(frame)
#     cv2.imshow(' frame ' , frame)

#     if cv2.waitKey(1) & 0xFF == ord ( 'q'):
#         break

# cap.release()
# out.release()
# cv2.destroyAllWindows()
