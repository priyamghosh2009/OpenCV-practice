import cv2
import random
img=cv2.imread('assets/1.png',1)
img=cv2.resize(img,(1000,1000),fx=0.01,fy=0.01)
cpy=img[100:300,100:500]
img[400:600,600:1000]=cpy
cv2.imshow("7.py",img)
cv2.waitKey(0)
cv2.destroyAllWindows()