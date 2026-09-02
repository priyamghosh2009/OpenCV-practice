import cv2
img=cv2.imread('assets/1.png',1)
img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
img1=cv2.cvtColor(img,cv2.COLOR_BGR2LAB)
cv2.imwrite('assets/1_bgr_to_lab.png',img1)
cv2.imshow("Priyam",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()