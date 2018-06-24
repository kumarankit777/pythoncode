#!/usr/bin/python

import cv2
import numpy
#to print all directories present in cv2 module
#print dir(cv2)

#reading image
#image name,image features

img=cv2.imread("cat.jpg",1)

#to draw line on image
#       data,startingpoint,color,line width

cv2.line(img,(6,9),(134,177),(120,210,180),4)

#to draw rectangle on image

cv2.rectangle(img,(40,20),(120,140),(60,90,190),3)

#to draw circle on image

cv2.circle(img,(20,30),25,(110,223,225),-5)

#to draw polyline on image
vrx=numpy.array(([20,80],[60,50],[100,80],[80,120],[40,140]), numpy.int32)
vrx=vrx.reshape((-1,1,2))
img=cv2.polylines(img,[vrx],True,(0,255,255),3)


#deciding font type

font=cv2.FONT_HERSHEY_SIMPLEX

#writing text on image
#            data,text,starting point,fonttype,size,color,linetype

cv2.putText(img,"WOW",(500,250),font,5,(0,0,255),lineType=cv2.LINE_AA)

#to show image

cv2.imshow("lineimg",img)

#to save the photo

cv2.imwrite("catline.jpg",img)


#to hold the upper window


cv2.waitKey(0)

#wait key will be destroy by q button

cv2.destroyAllWindows()
