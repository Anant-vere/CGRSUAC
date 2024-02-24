
import cv2
import numpy as np
import mediapipe as mp
import keyboard
import sys
import win32api
from collections import deque
import pyautogui
import pygetwindow
from PIL import Image
from datetime import datetime
import os
import subprocess
import screenshot
import copyfunc
import wordauto
import ocr2










bpoints = [deque(maxlen=1024)]
gpoints = [deque(maxlen=1024)]
rpoints = [deque(maxlen=1024)]
ypoints = [deque(maxlen=1024)]



blue_index = 0
green_index = 0
red_index = 0
yellow_index = 0

 
kernel = np.ones((5,5),np.uint8)

colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 255, 255)]
colorIndex = 0


paintWindow = np.zeros((471,636,3)) + 255



cv2.namedWindow('Paint', cv2.WINDOW_AUTOSIZE)



mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mpDraw = mp.solutions.drawing_utils



cap = cv2.VideoCapture(0)
ret = True
while ret:
    
    ret, frame = cap.read()

    x, y, c = frame.shape


    
    frame = cv2.flip(frame, 1)
    #hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    frame = cv2.rectangle(frame, (10,1), (80,65), (0,0,0), 2)
    frame = cv2.rectangle(frame, (100,1), (170,65), (255,0,0), 2)
    frame = cv2.rectangle(frame, (190,1), (260,65), (0,255,0), 2)
    frame = cv2.rectangle(frame, (280,1), (350,65), (0,0,255), 2)
    frame = cv2.rectangle(frame, (370,1), (440,65), (0,255,255), 2)
    frame = cv2.rectangle(frame, (460,1), (530,65), (0,0,0), 2)
    frame = cv2.rectangle(frame, (550,1), (620,65), (0,0,0), 2)

    cv2.putText(frame, "CLEAR", (20, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, "BLUE", (115, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, "GREEN", (200, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, "RED", (300, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, "YELLOW", (375, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, "S.S", (480, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, "OCR", (570, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)


    #frame = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    
    result = hands.process(framergb)

    
    if result.multi_hand_landmarks:
        landmarks = []
        for handslms in result.multi_hand_landmarks:
            for lm in handslms.landmark:
                # # print(id, lm)
                # print(lm.x)
                # print(lm.y)
                lmx = int(lm.x * 640)
                lmy = int(lm.y * 480)

                landmarks.append([lmx, lmy])


            
            mpDraw.draw_landmarks(frame, handslms, mpHands.HAND_CONNECTIONS)
        fore_finger = (landmarks[8][0],landmarks[8][1])
        center = fore_finger
        thumb = (landmarks[4][0],landmarks[4][1])
        cv2.circle(frame, center, 3, (0,255,0),-1)
        print(center[1]-thumb[1])
        if (thumb[1]-center[1]<30):
            bpoints.append(deque(maxlen=512))
            blue_index += 1
            gpoints.append(deque(maxlen=512))
            green_index += 1
            rpoints.append(deque(maxlen=512))
            red_index += 1
            ypoints.append(deque(maxlen=512))
            yellow_index += 1

        elif center[1] <= 65:
            if 10 <= center[0] <= 80: # Clear Button
                bpoints = [deque(maxlen=512)]
                gpoints = [deque(maxlen=512)]
                rpoints = [deque(maxlen=512)]
                ypoints = [deque(maxlen=512)]

                blue_index = 0
                green_index = 0
                red_index = 0
                yellow_index = 0

                paintWindow[67:,:,:] = 255
            elif 100 <= center[0] <= 170:
                    colorIndex = 0 # Blue
            elif 190 <= center[0] <= 260:
                    colorIndex = 1 # Green
            elif 280 <= center[0] <= 350:
                    colorIndex = 2 # Red
            elif 370 <= center[0] <= 440:
                    colorIndex = 3 # Yellow
            elif 460 <= center[0] <= 530:
                y= datetime.today().strftime('%Y-%m-%d')
                path=f"C:/Users/anant/Desktop/{y}"
                if not os.path.exists(path):
                    os.makedirs(path)
                no_of_files= os.listdir(path)
                no_of_files= len(os.listdir(path))
        
                newpath=f"C:/Users/anant/Desktop/{y}/{no_of_files+1}.png"


                titles=pygetwindow.getAllTitles()
                window= pygetwindow.getWindowsWithTitle('Paint')[0]
        


                left, top = window.topleft
                right,bottom= window.bottomright

                pyautogui.screenshot(newpath)
                im=Image.open(newpath)
                im=im.crop((left, top, right, bottom))

                im.save(newpath)
                img=cv2.imread(newpath)
                cut_image =img[37:508, 10:645]
                cv2.imwrite(newpath,cut_image)
                img2= Image.open(newpath)
                img2.show(newpath)
                
            
            elif 550 <= center[0] <= 620:
                newpath=("person.jpg")
                y= datetime.today().strftime('%Y-%m-%d')
                path=f"C:/Users/anant/Desktop/{y}"
                if not os.path.exists(path):
                    os.makedirs(path)
                no_of_files= os.listdir(path)
                no_of_files= len(os.listdir(path))
                    
                newpath=f"C:/Users/anant/Desktop/{y}/{no_of_files+1}.png"


                titles=pygetwindow.getAllTitles()
                window= pygetwindow.getWindowsWithTitle('Paint')[0]
                    


                left, top = window.topleft
                right,bottom= window.bottomright

                pyautogui.screenshot(newpath)
                im=Image.open(newpath)
                im=im.crop((left, top, right, bottom))

                im.save(newpath)
                img=cv2.imread(newpath)
                cut_image =img[37:508, 10:645]
                cv2.imwrite(newpath,cut_image)
                img2= Image.open(newpath)
                ocr2.ocr(newpath)
                
                 

                



        else :
            if colorIndex == 0:
                bpoints[blue_index].appendleft(center)
            elif colorIndex == 1:
                gpoints[green_index].appendleft(center)
            elif colorIndex == 2:
                rpoints[red_index].appendleft(center)
            elif colorIndex == 3:
                ypoints[yellow_index].appendleft(center)
    
    else:
        bpoints.append(deque(maxlen=512))
        blue_index += 1
        gpoints.append(deque(maxlen=512))
        green_index += 1
        rpoints.append(deque(maxlen=512))
        red_index += 1
        ypoints.append(deque(maxlen=512))
        yellow_index += 1

    
    points = [bpoints, gpoints, rpoints, ypoints]
    # for j in range(len(points[0])):
    #         for k in range(1, len(points[0][j])):
    #             if points[0][j][k - 1] is None or points[0][j][k] is None:
    #                 continue
    #             cv2.line(paintWindow, points[0][j][k - 1], points[0][j][k], colors[0], 2)
    for i in range(len(points)):
        for j in range(len(points[i])):
            for k in range(1, len(points[i][j])):
                if points[i][j][k - 1] is None or points[i][j][k] is None:
                    continue
                cv2.line(frame, points[i][j][k - 1], points[i][j][k], colors[i], 8)
                cv2.line(paintWindow, points[i][j][k - 1], points[i][j][k], colors[i], 8)

    cv2.imshow("Output", frame) 
    cv2.imshow("Paint", paintWindow)

    if cv2.waitKey(1) == ord('q'):
        screenshot.screenshot()

    if cv2.waitKey(1) == ord('c'):
        h=f"C:/Users/anant/Desktop/2023-04-28/1.png"

        subprocess.call(f"C:/Windows/system32/WindowsPowerShell/v1.0/powershell.exe  Set-Clipboard -Path {h}", shell=True)

    if cv2.waitKey(1) == ord('x'):
        copyfunc.copy()

    if cv2.waitKey(1) == ord('w'):
        wordauto.wordnotes()


        





        

    


        





                


        

cap.release()
cv2.destroyAllWindows()

        





            



    

