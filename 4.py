import cv2
img=cv2.imread('assets/1.png',-1)
img=cv2.resize(img,(0,0),fx=0.09,fy=0.09)
img=cv2.rotate(img,cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imwrite('assets/New_img.jpg',img)
cv2.imshow("Priyam_90CC",img)
cv2.waitKey(0)
cv2.destroyAllWindows()