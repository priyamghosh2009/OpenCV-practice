import cv2
cap=cv2.VideoCapture(0)
# Create a resizable window
cv2.namedWindow("Hello-CCTV", cv2.WINDOW_NORMAL)

# Start fullscreen
cv2.setWindowProperty(
    "Hello-CCTV",
    cv2.WND_PROP_FULLSCREEN,
    cv2.WINDOW_FULLSCREEN
)
while True:
    ret,frame=cap.read()  
    img=cv2.rectangle(frame,(10,10),(90,90),(0,0,255),-1)
    cv2.imshow("Hello-CCTV",img)
    if cv2.waitKey(1)==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()