from __future__ import print_function
import cv2 as cv
import requests

def detectAndDisplay(frame):
    headers = {
        'content-type': 'application/vnd.kafka.json.v2+json', 
    }

    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame_gray = cv.equalizeHist(frame_gray)
    #-- Detect faces
    faces = face_cascade.detectMultiScale(frame_gray)
    i = 0
    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        i +=1
    
    if i >= 1:
        print(i ,'face(s) detected')
        data = '{ "records": [ { "key": "key-1", "value": "%d face-detected" } ] }' % (i)

        response = requests.post('http://my-bridge-bridge-service-opencv-demo.apps.ocp.ws.local/topics/my-topic', headers=headers, data=data)
        
    cv.imshow('Capture - Face detection', frame)

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_alt.xml')

#-- 2. Read the video stream
cap = cv.VideoCapture(0)
if not cap.isOpened:
    print('--(!)Error opening video capture')
    exit(0)
while True:
    ret, frame = cap.read()
    if frame is None:
        print('--(!) No captured frame -- Break!')
        break
    else:
        detectAndDisplay(frame)
    if cv.waitKey(10) == 27:
        break