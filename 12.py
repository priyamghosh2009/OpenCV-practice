import cv2
cap=cv2.VideoCapture(0)
width=int(cap.get(3))
height=int(cap.get(4))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(
    'recorded_video.mp4',
    fourcc,
    30,
    (width, height),
    True
)
while True:
    ret,frame=cap.read()
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    fc=cv2.line(gray,(0,height//2),(width,height//2),(0,0,255),10)
    out.write(fc)
    cv2.imshow("Hello-CCTV",fc)
    if cv2.waitKey(1)==ord('q'):
        break
cap.release()
out.release()
cv2.destroyAllWindows()