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
def screenshot():
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



