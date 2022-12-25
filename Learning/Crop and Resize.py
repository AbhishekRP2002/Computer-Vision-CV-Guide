import cv2
import numpy as np
import matplotlib.pyplot as plt


path = 'Images/test1.jpg'
img = cv2.imread(path)
print(img.shape)  # (height , width , channels
# print(img)



#Resize Imag
imgResize = cv2.resize(img , (1000 , 1000))  # (width , height)
# we can set the width and height manually as well
print(imgResize.shape)


#Crop Image
imgCrop = img[:920 , :1000]  # (height , width)

imgCropResize = cv2.resize(imgCrop  , (img.shape[1] , img.shape[0])) #resize back to original size

cv2.imshow('Original Image' , img)
cv2.imshow('Resized Image' , imgResize)
cv2.imshow('Crop Image' , imgCrop)
cv2.waitKey(0)