import cv2
import random
img=cv2.imread('assets/1.png',1)
img=cv2.resize(img,(0,0),fx=0.06,fy=0.06)
for i in range(200):
    for j in range(img.shape[1]):
        img[i][j]=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]
cv2.imshow("7.py",img)
cv2.waitKey(0)
cv2.destroyAllWindows()