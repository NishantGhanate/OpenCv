import cv2
import numpy as np

cap = cv2.VideoCapture('H:\Github\OpenCv\SelfDrivingCar\Videos\challenge.mp4')

# Define a kernel size and apply Gaussian smoothing
kernel_size = 5

# Define our parameters for Canny and apply
low_threshold = 50
high_threshold = 180

# Next we'll create a masked edges image using cv2.fillPoly()
ignore_mask_color = 255   


# Define the Hough transform parameters
# Make a blank the same size as our image to draw on
rho = 1 # distance resolution in pixels of the Hough grid
theta = np.pi/180 # angular resolution in radians of the Hough grid
threshold = 1     # minimum number of votes (intersections in Hough grid cell)
min_line_length = 5 #minimum number of pixels making up a line
max_line_gap = 1    # maximum gap in pixels between connectable line segments


def Hough(masked_edges ,line_image):
    # Run Hough on edge detected image
    # Output "lines" is an array containing endpoints of detected line segments
    lines = cv2.HoughLinesP(masked_edges, rho, theta, threshold, np.array([]),
                                min_line_length, max_line_gap)

    # Iterate over the output "lines" and draw lines on a blank image
    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line(line_image,(x1,y1),(x2,y2),(0,255,0),10)

    # Create a "color" binary image to combine with line image
    color_edges = np.dstack((edges, edges, edges)) 

    # Draw the lines on the edge image
    lines_edges = cv2.addWeighted(color_edges, 0.8, line_image, 1, 0) 
    return lines_edges



while True:
    ret , image = cap.read()
    gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    blur_gray = cv2.GaussianBlur(gray,(kernel_size, kernel_size),0)
    edges = cv2.Canny(blur_gray, low_threshold, high_threshold)
    
    # Next we'll create a masked edges image using cv2.fillPoly()
    mask = np.zeros_like(edges)

    # This time we are defining a four sided polygon to mask
    imshape = image.shape
    #vertices = np.array([[(0,imshape[0]),(0, 0), (imshape[1], 0), (imshape[1],imshape[0])]], dtype=np.int32)
    vertices = np.array([[(0,imshape[0]),(450, 290), (490, 290), (imshape[1],imshape[0])]], dtype=np.int32)
    cv2.fillPoly(mask, vertices, ignore_mask_color)
    masked_edges = cv2.bitwise_and(edges, mask)
    line_image = np.copy(image)*0 # creating a blank to draw lines on
    lines = Hough(masked_edges,line_image)
    
    # cv2.imshow(' frame ' , masked_edges)
    cv2.imshow(' frame ' , lines)

    if cv2.waitKey(1) & 0xFF == ord ( 'q'):
        break



cap.release()
cv2.destroyAllWindows()
