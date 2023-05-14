import cv2
from pyzbar.pyzbar import decode
import time

cam = cv2.videoCapture(0)
cam.set(5,640)
cam.set(6,480)

camera = True
while camera == True:
    success, frame = cam.read()
    
    for i decode(frame):
    print(i.type)
    print(i.data.decode('utf-8'))
    time.sleep(6)
    cv2.imshow("Our_QR_code_scanner", frame)
    cv2.waitKey(3)

