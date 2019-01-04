import cv2
import os
import pytesseract

# First ddiwnload andd install  : windows download : https://github.com/UB-Mannheim/tesseract/wiki

# set file path 
pytesseract.pytesseract.tesseract_cmd = 'H:\Program Files (x86)\Tesseract-OCR\\tesseract.exe'

# copy : H:\Program Files (x86)\Tesseract-OCRtests\eng.traineddata 
# paste to : H:\Program Files (x86)\Tesseract-OCR
# Define config parameters.
# '-l eng'  for using the English language
# '--oem 1' sets the OCR Engine Mode to LSTM only.
#
#  There are four OCR Engine Mode (oem) available
#  0    Legacy engine only.
#  1    Neural nets LSTM engine only.
#  2    Legacy + LSTM engines.
#  3    Default, based on what is available.
#
#  '--psm 3' sets the Page Segmentation Mode (psm) to auto.
#  Other important psm modes will be discussed in a future post.  


# give image path
imPath = "H:\Github\OpenCv\OpticalCharacterRecognition\Google.png"

# load config for langauge and engine to use
config = ('-l eng --oem 1 --psm 3')

img = cv2.imread(imPath, cv2.IMREAD_COLOR)
# cv2.imshow(" " ,img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Run tesseract OCR on image
text = pytesseract.image_to_string(img, config=config)
# Print recognized text
print(text)








