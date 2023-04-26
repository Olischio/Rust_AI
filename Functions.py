import cv2
import numpy as np
from PIL import ImageGrab
import time
import pyautogui

def screenshot(amount, delay):
    for i in range(amount):
            
        #Tar bilde og konverterer til Numpy array
        screenshot = ImageGrab.grab()
        screenshot_np = np.array(screenshot)

        #Lagrer filen
        cv2.imwrite(f'screenshot/screenshot{i}.jpg', screenshot_np)
        
        time.sleep(delay)


def moveMouse(Circle_Coordinates):
    pyautogui.moveTo(Circle_Coordinates)
    
    with pyautogui.hold('left'):
        pyautogui.time.sleep(1)
    