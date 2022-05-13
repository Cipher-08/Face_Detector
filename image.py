#importing open cv 
import cv2 as cv
from random import randrange

#algoriuthm for detecting faces 
train_face_data = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

#Devoting or assigning images to variables
# img1 = cv.imread('elon_h.jpg')
img2 = cv.imread('group.png')

#Convert the coloured images to greayscale
grayscaled_img = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)
# grayscaled_img1 = cv.cvtColor(img1,cv.COLOR_BGR2GRAY)


#tracking data using algorithm imported 
face_coordinates = train_face_data.detectMultiScale(grayscaled_img)
# print(face_coordinates)


for (x,y,w,h) in face_coordinates:
    cv.rectangle(img2,(x,y),(x+w,y+h),(randrange(128,256),randrange(128,256),randrange(128,256)),4)
# Draw rectangles around the faces whih we have detected in the face_coordinates 



ma = cv.imread('')


#To display the image
cv.imshow("YEAH",img2)

#As the image opens closed within a second this key gives it the time to be executed
cv.waitKey()
