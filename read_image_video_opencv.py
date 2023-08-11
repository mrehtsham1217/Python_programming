# import cv2 as cv
# --->This is how image is read in python using cv2---->
# img = cv.imread("images/doll.jpeg")
# img2 = cv.imread("images/img2.jpg")
# cv.imshow('cat', img2)

# --->This is how video is read in python using cv2---->
import numpy as np
import cv2

cap = cv2.VideoCapture('Videos/nature.mp4')
while (True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()  # cv.waitKey(0)
