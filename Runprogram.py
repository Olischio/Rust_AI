from roboflow import Roboflow
import cv2 as cv2
import os
import numpy as np
from PIL import ImageGrab
import time as T
import pyautogui

import Functions as F
import V5omg as V5


def RunProgram():

    numberScreenshots = 3
    numberDelay = 2

    F.screenshot(numberScreenshots, numberDelay)

    time = numberScreenshots * numberDelay

    T.sleep(time)

    V5.Run()

    F.moveMouse()

RunProgram()
