import cv2
import numpy as np
kernel = np.ones((5,5) , np.uint8)  # 5,5 is the kernel size , np.uint8 is the datatype))


path = 'Images/test1.jpg'
img = cv2.imread(path)
cv2.imshow( 'Original Image' , img)
cv2.waitKey(0)


#Convert to grayscale
img3 = cv2.imread(path , 0)  # 0 for grayscale
img2 = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)  # while using web cam / Video stream  we can use this 

cv2.imshow('Grayscale Image' , img2)
cv2.waitKey(0)


#Add Blur to the image
imgBlur = cv2.GaussianBlur(img , (15,15) , 0)  # 7,7 is the kernel size , 0 is the sigmaX
cv2.imshow('Blur Image' , imgBlur)
cv2.waitKey(0)



#Edge Detection
imgCanny = cv2.Canny(img , 100 , 100)  # 100 is the threshold1 , 100 is the threshold2
cv2.imshow('Canny Image' , imgCanny)
cv2.waitKey(0)  # 0 for infinite time

#Image Dilation and Image Errosion
imgDilation = cv2.dilate(imgCanny , kernel , iterations = 3)  # 1 is the number of iterations
cv2.imshow('Dilated Image' , imgCanny)
cv2.waitKey(0) # 0 for infinite time

#Image Erosion
imgErosion = cv2.erode(imgCanny , kernel , iterations = 1) # 1 is the number of iterations

cv2.imshow('Erosion Image' , imgErosion)
cv2.waitKey(0) # 0 for infinite time
