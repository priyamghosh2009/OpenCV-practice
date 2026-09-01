import numpy as np
import cv2
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    height=int(cap.get(4))
    width=int(cap.get(3))
    image=np.zeros(frame.shape,np.uint8)
    sframe=cv2.resize(frame,(0,0),fx=0.5,fy=0.5)
    image[:height//2,:width//2]=cv2.rotate(sframe,cv2.ROTATE_180)
    image[:height//2,width//2:]=sframe
    image[height//2:,:width//2]=cv2.rotate(sframe,cv2.ROTATE_180)
    image[height//2:,width//2:]=sframe
    cv2.imshow('Frame',image)
    if cv2.waitKey(1)==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()