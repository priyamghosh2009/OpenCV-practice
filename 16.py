import cv2
import numpy as np
cap=cv2.VideoCapture(0)
height=int(cap.get(4))
width=int(cap.get(3))
while True:
    ret,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_blue=np.array([30,30,90])
    upper_blue=np.array([255,255,255])
    mask=cv2.inRange(hsv,lower_blue,upper_blue)
    pic_and=cv2.bitwise_and(frame,frame,mask=mask)
    pic_or=cv2.bitwise_or(frame,frame,mask=mask)
    pic=cv2.bitwise_not(frame,frame,mask=mask)
    cv2.imshow('Hello',pic)
    cv2.imshow("Hello_OR",pic_or)
    cv2.imshow("Hello_and",pic_and)
    if cv2.waitKey(1)==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()