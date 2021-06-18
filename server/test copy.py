# importing libraries
import cv2
import numpy as np
import dlib

# Create a VideoCapture object and read from input file
cap = cv2.VideoCapture(0)
# get the coordinate 
detector = dlib.get_frontal_face_detector()

# Check if camera opened successfully
if (cap.isOpened()== False):
    print("Error opening video file")

# Read until video is completed
while(cap.isOpened()):
	
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == True:

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector(gray)
        # Counter to count number of faces
        i = 0
        for face in faces:
            x, y = face.left(), face.top()
            x1, y1 = face.right(), face.bottom()
            cv2.rectangle(frame, (x, y), (x1, y1), (0, 255, 0), 2)

            # Increment the iterartor each time you get the coordinates
            i = i+1

            # Adding face number to the box detecting faces
            cv2.putText(frame, 'face num'+str(i), (x-10, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            print(face, i)

        # Display the resulting frame
        cv2.imshow('frame', frame)

        # Press Q on keyboard to exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # Break the loop
    else:
        break

# When everything done, release
# the video capture object
cap.release()

# Closes all the frames
cv2.destroyAllWindows()
