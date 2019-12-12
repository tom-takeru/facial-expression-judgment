#import modules
import numpy as np
import cv2

#input filename
file_path = "./sample_images/" + input()

#load image
img = cv2.imread(file_path)

#grayscale conversion
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#show image 
cv2.imshow('img', img)
cv2.waitKey(0)

#load haarcascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#detect faces
faces = face_cascade.detectMultiScale(img_gray, 1.3, 5)

#draw rectangles on faces 
for (x, y, w, h) in faces:
    img = cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

#show face-detected image
cv2.imshow('img', img)
cv2.waitKey(0)

#close all windows
cv2.destroyAllWindows()
