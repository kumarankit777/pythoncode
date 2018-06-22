#!/usr/bin/python2

import  cv2

#  laoding  image 
img=cv2.imread('cat.jpg')
img1=cv2.imread('cat.jpg',0)

#  Print  height and width
print  img.shape

#  to display that image 
cv2.imshow("cat",img)
cv2.imshow("catnew",img1)

#  image window holder activate 
cv2.waitKey(0)
#  waitkey will destroy  by using  q  button
cv2.destroyAllWindows()


