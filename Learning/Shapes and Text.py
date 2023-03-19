import cv2
import numpy as np
import matplotlib.pyplot as plt


img = np.zeros((512,512,3), np.uint8)
print(img.shape)
img1 = np.ones((512 , 512 , 3) , np.uint8)
# Both will lead to  black image of shape 512 , 512 , 3

img[:] = 255 , 0 , 0 # Color of the image changed to Blue

cv2.line(img , (0,0) , (img.shape[1] , img.shape[0]) , (0,255,0) , 3)

cv2.rectangle(img , (0,0) , (250,250) , (0,0,255) , 2)
cv2.rectangle(img , (0,0) , (100,100) , (0,255,0) , cv2.FILLED);
cv2.circle(img , (200,50) , 30 , (255,255,0) , 5)
cv2.putText(img , " OpenCV Text here" , (100,200) , cv2.FONT_HERSHEY_COMPLEX , 1 , (0,150,0) , 1)

cv2.imshow("Image" , img)
# cv2.imshow("Image Temp" , img1)
cv2.waitKey(0)
