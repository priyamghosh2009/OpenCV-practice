import cv2
cap=cv2.VideoCapture(0)
height=int(cap.get(4))
width=int(cap.get(3))
while True:
    ret,frame=cap.read()
    img=cv2.circle(frame,(height//2,width//2),30,(0,0,255),-1)
    cv2.imshow("Hello",img)
    if cv2.waitKey(1)==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
