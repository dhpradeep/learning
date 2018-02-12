#Pedestrian Detection Program
import cv2
import time
import numpy as np

#body classifeir for haarcascade_fullbody.xml file
body_classifier=cv2.CascadeClassifier("haarcascade_fullbody.xml")

#initiate video capture for video file
cap=cv2.VideoCapture("Pedestrian-2.mp4")

while cap.isOpened():
    #Read first Frame
    time.sleep(.001)
    ret, frame=cap.read()
#     if ret==True:
    frame=cv2.resize(frame, None, fx=0.5,fy=0.5,interpolation=cv2.INTER_LINEAR)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        #pass frame to our video
    bodies=body_classifier.detectMultiScale(gray,1.3,3)

        #extract data
    for(x,y,w,h) in bodies:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
        cv2.imshow("Pedestrians",frame)
    if cv2.waitKey(1)==13:
        break
#     else:
#         break
cap.release()
cv2.destroyAllWindows()
