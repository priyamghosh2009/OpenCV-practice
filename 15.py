import cv2
cap=cv2.VideoCapture(0)
height=int(cap.get(4))
while True:
    ret,frame=cap.read()
    font=cv2.FONT_HERSHEY_SIMPLEX
    img=cv2.putText(frame,'Priyam Ghosh    01-SEP-2026',(10,height-10),font,1,(0,0,0),2,cv2.LINE_AA)
    cv2.imshow("HELLO",img)
    if cv2.waitKey(1)==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()