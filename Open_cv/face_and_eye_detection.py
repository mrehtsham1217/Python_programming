import cv2
import time
cap = cv2.VideoCapture(0)
model = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")

count = 0
while True:
    _, img = cap.read()
    # convert the image into gray scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the face
    faces = model.detectMultiScale(gray, 1.1, 4)
    # eyes = eye_model.detectMultiScale(gray, 1.3, 4)
    # draw a rectangle around the face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 3)
        # for (ex, ey, ew, eh) in faces:
        #     cv2.rectangle(img_color, (ex, ey), (ex+ew, ey+eh), (0, 0, 255), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (255, 0, 0), 2)

        # Display the image
        cv2.imshow('img', img)
        t = time.strftime("%Y-%m-%d_%H_%M_S")

        print("image " + t + "Saved")
        file = "img"+t+".jpg"
        cv2.imwrite(file, roi_color)
        count += 1
        # You can stop
        stop = cv2.waitKey(30) & 0xff
        if stop == 27:
            break
cap.release()
