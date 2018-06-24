#!/usr/bin/python
import cv2
#all function of cv2 that is open cv
print dir(cv2)
#reading image 
#image name,image features
#we can write cv2.IMREAD_COLOR instead of 1
#cv2.IMREAD_BGR2GRA instead of 0
#cv2.IMREAD_UNCHANGE_COLOR instead of -1
img=cv2.imread("cat.jpg",1)
img1=cv2.imread("cat.jpg",0)
img2=cv2.imread("cat.jpg",-1)
#checking rows and coloumns
print img.shape
#to show images
cv2.imshow("boy",img)
cv2.imshow("bye",img1)
cv2.imshow("come",img2)
#to save black and white photo
cv2.imwrite("app.jpg",img1)
#to hold upper window      
cv2.waitKey(0)


