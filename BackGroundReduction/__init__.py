import cv2
import numpy as np
import matplotlib.pyplot as plt

#cap=cv2.VideoCapture('people-walking.mp4')
cap=cv2.VideoCapture(0)
fgbg=cv2.createBackgroundSubtractorMOG2()

#face tracking concept.
while True:
    ret, frame=cap.read()
    fgmask=fgbg.apply(frame)

    cv2.imshow('original',frame)
    cv2.imshow('fg',fgmask)

    k=cv2.waitKey(30) & 0xff
    if k==27:
        break

cap.release()
cv2.destroyAllWindows()