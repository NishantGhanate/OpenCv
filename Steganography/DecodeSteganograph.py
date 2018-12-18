
# coding: utf-8

# In[55]:


import cv2
import os
import re

scriptDir = os.path.dirname(os.path.realpath('__file__'))

working = 'H:\Github\OpenCv\Steganography\output.png'

img = cv2.imread('H:\Github\OpenCv\Research\images\Hiils_encoded.jpg')

imageHeight , imageWidth , Channel = img.shape

Blue , Green ,  Red = cv2.split(img)

# print(img)

def Dec2bin(n):
    x=n
    k=[]
    while (n>0): 
        a=int(float(n%2))
        k.append(a)
        n=(n-a)/2 
    string=""

    for j in k[::-1]:
        string=string+str(j)
    
    binaryLen = 8 - len(string)
    if binaryLen >= 1:
        for i in range(binaryLen):
            string = '0' + string
           
    return string


i = 0
binary = ''
Message =''
loop = True
count = 0

for h in range(imageHeight):
    if loop:
        for w in range(imageWidth):
            r =  Dec2bin(Red[h][w])
            binary = binary + r[-1]
            if loop:
                i = i + 1
                if i == 8:
                    msg = int(binary,2)
                    msg = chr(msg)
                    i = 0
                    binary = ''
                    if count <3 :
                        # print(msg)
                        if msg == '@':
                            count = count + 2 
                            # print(count)
                        Message = Message + msg
                        # print(Message)
                        msg = ''
                    else:
                        loop = False
                        break
            else:
                break

    else:
        break
                     


# Message = re.search('@.*?@',Message).group()
Message = Message.replace('@','')
print(Message)

