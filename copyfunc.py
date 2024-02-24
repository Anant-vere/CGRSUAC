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

def copy():
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
    im=Image.open (newpath)
    im=im.crop((left, top, right, bottom))
    im.save(newpath)
    im.show(newpath)

    subprocess.call(f"C:/Windows/system32/WindowsPowerShell/v1.0/powershell.exe  Set-Clipboard -Path {newpath}", shell=True)
    print("flag copy true")



