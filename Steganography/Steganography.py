
# coding: utf-8

# In[1]:


import cv2 
import re
import os


# In[2]:


img = cv2.imread("H:/Github/OpenCv/Research/images/bg5.jpg")

imageHeight , imageWidth , colorChannel = img.shape

print('Printing image size  Height = {} , Width = {} , Channel = {} '.format(imageHeight,imageWidth,colorChannel))


# In[3]:


print(img)


# In[4]:


Blue , Green , Red = cv2.split(img)
# printing Red channel because will after altering Red channels bits we can see the difference
# print(Red)


# In[5]:


# function to convert Decimal to binary which return 8-bits

def Dec2bin(n):
    x=n
    k=[]
    while (n>0):
        # print("value of n = {}".format(n))
        a=int(float(n%2))
        # print("n%2 = {}".format(a))
        k.append(a)
        n=(n-a)/2
        # print("(n-a)/2 = {}".format(n))
    string=""

    # print("k = {}".format(k) )
    # print(" String reverse k[::-1] = {}".format(k[::-1]) )
    
    
    for j in k[::-1]:
        print("value of j = {}".format(j))
        string=string+str(j)
    
    binaryLen = 8 - len(string)
    # print(binaryLen)
    if binaryLen >= 1:
        for i in range(binaryLen):
            string = '0' + string
            
    # print('The binary no. for %d is %s'%(x, string))
    return string


# In[6]:


msg = Dec2bin(65)
print(msg)


# In[7]:


secretMessage = "@This is very long secret message hidden ina imageof501x501@"

# Conversting String to ASCII CODE i.e @ = 64 , N = 74
secretMessage = [ord(s) for s in secretMessage]
# print("String @Nishant@ ASCII CODE = {}".format(secretMessage))
  


# In[8]:


# Converting it's ASCII CODE to Binary form 
secretMsgBin = [Dec2bin(s) for s in secretMessage]
# print("Binary form = {}".format(secretMsgBin))


# In[9]:


# Making a single array of sinle bit's so it will be easy loop over it

msgBits = []
for s in secretMsgBin:
    for b in s:
        msgBits.append(b)

# print("Message bits = {}".format(msgBits))
# print("Message len  = {}".format(len(msgBits)) ) 


# In[10]:


i = 0
msgBitsLen = len(msgBits)-1
Loop = True

# This loop will only loop the total length of message bits 
# Our image gives us 2-D Matrix Height and Wdith 

for h in range(imageHeight):
    if Loop:
        for w in range(imageWidth):
            print("Index = {} ".format(i) )
            if i <= msgBitsLen:
                # Converting decimal to binary of Red pixel 
                r = Dec2bin(Red[h][w])
                # print("r[-1] = {} , msg = {} ".format(r[-1] , msgBits[i] ))
                # Replacing last bits of Red pixel with our message bits
                r = re.sub(r[-1]+'$', msgBits[i] , r)
                # converting back decimal to binary and placing it back on its location 
                Red[h][w] = int(r,2) 
                # Here i is our counter for msgBits Array
                i = i + 1  
            else:
                # break the inner-loop as counter exceeds message length
                # make outer loop condtion Flase to break 
                Loop = False
                break
    else:   
        break
                     


# In[11]:


# Now you can see the diffrence in Red channel 
# print(Red)


# In[12]:


# Get our curring working Folder/Directory
scriptDir = os.path.dirname(os.path.realpath('__file__'))
# Merge back our RBG pixel 
# Note : OpenCv Reads and Write image in BGR Method (blue takes less amount of data that's why)
img1 = cv2.merge([Blue,Green,Red])
# finallay save our Encoded image
cv2.imwrite(scriptDir + os.path.sep +'home' + '.png' ,img1 )

