import cv2 
import numpy as np




face_cascade = cv2.CascadeClassifier(r"C:\Users\Darren\Documents\GitHub\DTY12\roadsigns\stopsign\classifier\cascade.xml")
img = cv2.imread(r"C:\Users\Darren\Documents\GitHub\DTY12\roadsigns\Stop_Sign_in_Australia.jpeg")
resized = cv2.resize(img,(840,480))
gray = cv2.cvtColor(resized,cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray,6.5,17)

for(x,y,w,h) in faces:
    resized=cv2.rectangle(resized,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow('img',resized)
cv2.waitKey(0)
cv2.destroyAllWindows()



