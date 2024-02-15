'''
Palce
'''
import cv2
import cvzone
from cvzone.FaceDetectionModule import FaceDetector
from cvzone.HandTrackingModule import HandDetector
from cvzone.FPS import FPS

fps = FPS(avgCount = 30)
capture = cv2.VideoCapture(0)
capture.set(100, 200)
hd = HandDetector(detectionCon = 0.6)

while True:
    _, img = capture.read()
    fps.update(img, pos=(490, 40), scale = 2, bgColor=(0,0,0))
    hand, img = hd.findHands(img)
    if hand:
        lefthand = hand[0]
        bbox = lefthand['bbox']
        lmlist = lefthand["lmList"]   
        handtype = lefthand["type"]
        fingersup = hd.fingersUp(lefthand)
        totalfingers = fingersup.count(1)
        cv2.putText(img, str(totalfingers), (30, 150), cv2.FONT_HERSHEY_PLAIN,3, (255, 0, 0), 12)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    cv2.imshow("Palce",img)

capture.release()
cv2.destroyAllWindows()