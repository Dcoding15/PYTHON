import cv2

#cv2.VideoCapture([path of video] / [int for camera])
cap = cv2.VideoCapture(0)
while True: 
    isT, vid = cap.read()                       # return bool, binary data
    cv2.imshow("Video", vid)
    if cv2.waitKey(20) & 0xFF == ord('d'):      #<-- Press D for exit
        break

cap.release()
