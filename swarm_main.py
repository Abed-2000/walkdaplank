import os
from dotenv import load_dotenv
import cv2
import swarm as swarm
import time
load_dotenv()

DEVICE_IP = os.getenv("DEVICE_IP")
CONTROL_CENTER_IP = os.getenv("CONTROL_CENTER_IP")

cap = cv2.VideoCapture(0)
human_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')

if not cap.isOpened():
    print(time.strftime('%a %H:%M:%S') + " Error: Trouble connecting to camera")
    swarm.publishControlCenter(time.strftime('%a %H:%M:%S') + " Error: Trouble connecting to camera on swarm device @ " + str(DEVICE_IP))
    exit()

while True:
    ret, frame = cap.read()
    swarm.send_video_feed(CONTROL_CENTER_IP)
    if not ret:
        print(time.strftime('%a %H:%M:%S') +" Error: Failed to capture a frame")
        swarm.publishControlCenter(time.strftime('%a %H:%M:%S') + " Error: Failed to capture a frame on swarm device @ " + str(DEVICE_IP))
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    humans = human_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    for (x, y, w, h) in humans:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        print(time.strftime('%a %H:%M:%S') + " Human Detected!")
        swarm.publishControlCenter(time.strftime('%a %H:%M:%S') + " Human Detected on swarm device @ " + str(DEVICE_IP))
    cv2.imshow('Camera', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()