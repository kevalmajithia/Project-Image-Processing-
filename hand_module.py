import cv2 as cv 
import time 
import mediapipe as mp 
cap = cv.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
pTime = 0
cTime = 0
while True: 
    success, img=cap.read()
    imgRGB = cv.cvtColor(img,cv.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)
    # getting the fps for the hand tracking model 
    cTime = time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    cv.putText(img,str(int(fps)),(10,70),cv.FONT_HERSHEY_SIMPLEX,3,(0,0,255),3)
    cv.imshow("Live Feed",img)
    cv.waitKey(1)
