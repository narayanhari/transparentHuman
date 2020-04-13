import cv2
import numpy as np
import copy
cap= cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('a.avi', fourcc, 5.0, (640, 480))
status,pic=cap.read()
cv2.imshow('hi',pic)
cv2.waitKey()
black=(150,150,150)
while True:
    status,photo=cap.read()
    for i in range(photo.shape[0]):
        for j in range(photo.shape[1]):
            if photo[i,j,0]<black[0] and photo[i,j,1]<black[1] and photo[i,j,2]<black[2]:
                photo[i,j]=pic[i,j]
    out.write(photo)
    cv2.imshow('hi',photo)
    if cv2.waitKey(10)==13:
        break
cv2.destroyAllWindows()
cap.release()
out.release()