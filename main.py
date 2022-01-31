from cvzone.HandTrackingModule import HandDetector
import cv2
from pandas import Interval
import pyautogui
from math import hypot



def right(fin, lmList):
            if fin==[0,1,1,0,0]:    
                return pyautogui.hotkey("w")
            if fin==[1,0,0,0,0]:    
                return pyautogui.hotkey("a")
            if fin==[0,0,0,0,1]:    
                return pyautogui.hotkey("d")
            if fin==[0,1,1,1,0]:    
                return pyautogui.hotkey("s")
            if fin==[1,1,1,1,1]:
                return pyautogui.hotkey(" ")    
            # x1,y1 = lmList[12][0],lmList[12][1]
            # x2,y2 = lmList[8][0],lmList[8][1] 
            # length = hypot(x2-x1,y2-y1)
            # if length<=1:
                
            #         if fin==[0,1,1,0,0]:    
            #            return pyautogui.hotkey("w"+"shift")
            #         if fin==[1,0,0,0,0]:    
            #             return pyautogui.hotkey("a")
            #         if fin==[0,0,0,0,1]:    
            #             return pyautogui.hotkey("d")
            #         if fin==[0,1,1,1,0]:    
            #             return pyautogui.hotkey("s")

def left(fin, lmList):
    if fin[1]==1:
        x1, y1 = lmList[13]
        return pyautogui.click(button='left', clicks=2, interval=0.25), pyautogui.moveTo(x1,y1,duration=0.1)
    if fin[0]==1:
        
        return pyautogui.click(button='right', clicks=1)



cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=2)
while True:
    # Get image frame
    success, img = cap.read()
    # Find the hand and its landmarks
    hands, img = detector.findHands(img)  # with draw
    # hands = detector.findHands(img, draw=False)  # without draw

    if hands:

        if len(hands) == 1:
        # Hand 1
            hand1 = hands[0]
            lmList1 = hand1["lmList"]  # List of 21 Landmark points
            bbox1 = hand1["bbox"]  # Bounding box info x,y,w,h
            centerPoint1 = hand1['center']  # center of the hand cx,cy
            handType1 = hand1["type"]  # Handtype Left or Right

            fingers1 = detector.fingersUp(hand1)
            if handType1 == 'Right':
                right(fingers1, lmList1)

        
            elif handType1 == 'Left':
                left(fingers1, lmList1)
                # x1, y1 = lmList1[9][1],lmList1[9][2]
                # pyautogui.moveTo(x1, y1, duration = 0.1)
            



        if len(hands) == 2:
            # Hand 2
            hand2 = hands[1]
            lmList2 = hand2["lmList"]  # List of 21 Landmark points
            bbox2 = hand2["bbox"]  # Bounding box info x,y,w,h
            centerPoint2 = hand2['center']  # center of the hand cx,cy
            handType2 = hand2["type"]  # Hand Type "Left" or "Right"
            fingers2 = detector.fingersUp(hand2)

            if handType2 == 'Right':
                right(fingers2, lmList2)
            elif handType2 == 'Left':
                left(fingers2, lmList2)

            hand3 = hands[0]
            lmList3 = hand3["lmList"]  # List of 21 Landmark points
            bbox3 = hand3["bbox"]  # Bounding box info x,y,w,h
            centerPoint3 = hand3['center']  # center of the hand cx,cy
            handType3 = hand3["type"]  # Hand Type "Left" or "Right"
            fingers3 = detector.fingersUp(hand3)

            if handType3 == 'Right':
                right(fingers3, lmList3)
            elif handType3 == 'Left':
                left(fingers3, lmList3)

            

            # Find Distance between two Landmarks. Could be same hand or different hands
            # length, info, img = detector.findDistance(lmList1[8], lmList2[8], img)  # with draw
            # length, info = detector.findDistance(lmList1[8], lmList2[8])  # with draw
    # Display
    
    cv2.imshow('Image',img)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break   
# cap.release()
# cv2.destroyAllWindows()
