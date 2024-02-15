'''
Detekcja twarzy
'''
import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

camera = cv2.VideoCapture(0)

while cv2.waitKey(1) == -1:
    success, img = camera.read()
    img = cv2.flip(img, 2)
    if success:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5, minSize=(120,120))
        for(x, y, w, h) in faces:
            cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)

            gray2 = gray[y: y+h, x: x+w]
            eyes = eye_cascade.detectMultiScale(gray2, 1.03, 5, minSize=(40, 40))
            for(ex, ey, ew, eh) in eyes:
                cv2.rectangle(img, (x+ex, y+ey), (x+ex+ew, y+ey+eh), (0, 0, 255), 2)

        cv2.imshow("Wykrywanie twarzy", img)