import cv2
img=cv2.imread('assets/1.png',1)
img=cv2.resize(img,(0,0),fx=0.05,fy=0.05)
cv2.imshow("IMAGE-PRIYAM",img)
cv2.waitKey(0)
cv2.destroyAllWindows()