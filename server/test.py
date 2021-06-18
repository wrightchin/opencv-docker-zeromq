from __future__ import print_function
import cv2 as cv
import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://client:5001")
# socket.bind("tcp://*:5001")
# socket.connect("tcp://0.0.0.0:5001")
# context = zmq.Context()
# socket = context.socket(zmq.PUB)
# socket.bind("tcp://*:5001")

def detectAndDisplay(frame):
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame_gray = cv.equalizeHist(frame_gray)
    #-- Detect faces
    faces = face_cascade.detectMultiScale(frame_gray)
    i = 0
    for (x, y, w, h) in faces:
        # center = (x + w//2, y + h//2)
        # frame = cv.rectangle(frame, center, (w//2, h//2), 0, 0, 360, (255, 0, 255), 4)
        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        i +=1
    
    if i >= 1:
        print(i ,'face(s) detected')
        i_string = str(i)
        socket.send(i_string.encode('utf-8'))
        # socket.send_string(i_string)

        message = socket.recv()
        # print(f"Received reply {message} ]")
        
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