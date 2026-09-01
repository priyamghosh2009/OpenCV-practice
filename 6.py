import cv2
img=cv2.imread('assets/1.png',1)
#print(img[0])
#print(img[0][0])
print(img[0][0][0])
img[0][0][0]=255