#Fishbot FiveM by ReVeR
from pyautogui import *
import pyautogui
from python_imagesearch.imagesearch import *
import time
import keyboard
import random
import cv2
import os
import numpy as np
import pyscreenshot as ImageGrab
coiledestiny = input("Podaj co ile złowionych ryb mają wykonywać się zdjęcia: ")
dokladnosc = input("Podaj dokladnosc pomiaru: ")


count = 0
coile = 0
while True:
    start_time = time.time()

    list = os.listdir(r'.\images')
    lernscreencount = len(list)

    imagecount = 0
    breakpt = 0
    pytable = []


    for image in list:
        patch: str = r'.\images' + "\\" +image
        pytable.append(pyautogui.locateOnScreen(patch, region=(455, 100, 500, 500), grayscale=False, confidence=0.5))
        imagecount = imagecount + 1


    img = pyautogui.screenshot(region=(455, 100, 500, 500))
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    if cv2.waitKey(1) == ord("q"):
        break

    for pycords in pytable:
        if pycords != None:
            x, y, w0, h0 = pycords
            x1 = x - 455
            y1 = y - 100
            w1 = x1 + w0
            h1 = y1 + h0
            start = (x1, y1)
            end = (w1, h1)
            frame = cv2.rectangle(frame, start, end, (0, 0, 255), 2)
            breakpt = breakpt + 1
            coile = coile + 1

        if lernscreencount < 20 and coile == int(coiledestiny):
            imgnew = pyautogui.screenshot(region=(x, y, w0, h0))
            i = imagecount + 1 + 10
            imgnew.save(r".\images\r"+str(i)+".png")
            coile = 0
            break

        if breakpt > int(dokladnosc):
            timereduce = (time.time() - start_time)
            if timereduce<1:
                timereduce=1
            time.sleep(6-timereduce)
            keyboard.press('e')
            time.sleep(0.1)
            keyboard.release('e')
            breakpt = 0
            count = count + 1
            break

    font = cv2.FONT_HERSHEY_SIMPLEX
    bottomLeftCornerOfText = (10, 450)
    fontScale = 1
    fontColor = (0, 0, 255)
    lineType = 2
    text = 'Ilosc zlowionych ryb: ' + str(count)
    cv2.putText(frame,text,bottomLeftCornerOfText,font,fontScale,fontColor,lineType)
    cv2.imshow("screenshot", frame)

cv2.destroyAllWindows()


