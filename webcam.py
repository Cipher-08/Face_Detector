#importing open cv 
import cv2 as cv
from random import randrange
train_face_data = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
webcam = cv.VideoCapture(0)
while True:
    succesful_frame_read,frame = webcam.read()
    grayscaled_img = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    face_coordinates = train_face_data.detectMultiScale(grayscaled_img)
    for (x,y,w,h) in face_coordinates:
         cv.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),4)
    cv.imshow("YEAH",frame)
    key = cv.waitKey(1)
    if key==81 or key==113:
        break


webcam.release()

