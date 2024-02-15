'''
Obsługa kamery
'''
import cv2
capture = cv2.VideoCapture(0)
capture.set(3, 1200)
capture.set(cv2.CAP_PROP_BRIGHTNESS, 10)

while True:
    success, img = capture.read()
    img = cv2.flip(img, 1)
    cv2.imshow("Kamerka", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break