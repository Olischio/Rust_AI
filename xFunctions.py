import cv2 as cv2
import os
import numpy as np
from PIL import ImageGrab as imagegrab
import pyautogui as gui
import time
from roboflow import Roboflow
import random
import math
import secret

def modelOG():
        
    rf = Roboflow(api_key=secret.key)
    project = rf.workspace().project("rustirn_mega")
    model = project.version(1).model

    #pathToImagesFolder = "C:\\Users\\Oliver S\\OneDrive - Osloskolen\\Desktop\\RustAI"


    for filename in os.listdir("screenshot"):
        img = cv2.imread(os.path.join("screenshot", filename))
        if img is not None:

            prediction = (model.predict(os.path.join("screenshot", filename), confidence=10, overlap=0).json())
            #print(prediction)

            predictions = prediction['predictions']
            print("---PREDICITONS---")
            print(predictions)

            preds_x = []
            preds_y = []
            height = []
            width = []
            for result in predictions:
                preds_x.append(result['x'])
                preds_y.append(result['y'])
                height.append(result['height'])
                width.append(result['width'])

            print(f"Coordinates x {preds_x} y {preds_y} Height & Width {height} {width}")

            image_path = "C:\\Users\\Oliver S\\OneDrive - Osloskolen\\Desktop\\RustAI\\prediction.jpg"

            open("screenshot\\prediction.jpg", "w+").close()
            draw_circles_on_bounding_boxes(os.path.join("screenshot", filename), predictions)

        return preds_x, preds_y
            
        

def screenshot(amount, delay):
    for i in range(amount):
            
        screenshot = imagegrab.grab()
        screenshot_np = np.array(screenshot)
        cv2.imwrite(f'screenshot/screenshot{i}.jpg', screenshot_np)
        
        time.sleep(delay)

# screenshot(3,1)

def draw_circles_on_bounding_boxes(image_path, predictions):
            # Get the image dimensions
            image = cv2.imread(image_path)

            # Loop over the predictions and draw circles on each bounding box
            for prediction in predictions:
                x = prediction['x']
                y = prediction['y']
                w = prediction['width']
                h = prediction['height']

                # Calculate the center coordinates of the bounding box
                cx = x + (w // 20)
                cy = y + (h // -7)

                cx = int(cx)
                cy = int(cy)

                image = cv2.circle(image, (cx, cy), 15, (255, 0, 0), 2)

            cv2.imshow("Bounding Boxes", image)
            cv2.waitKey(0)

        # open("screenshot\\prediction.jpg", "w+").close()
        # draw_circles_on_bounding_boxes(os.path.join("screenshot", filename), predictions)

def movemouse(x, y):
    gui.moveTo(x,y)
    gui.hold(2)

def movemouse2(x_list, y_list):
     for x, y in zip(x_list, y_list):
          gui.moveTo(x, y)
          gui.hold(2)

def movemouse3(x_list, y_list):
    for x, y in zip(x_list, y_list):
        gui.moveTo(x, y)
        gui.moveRel(0, 50) # move mouse up by 50 pixels
        gui.moveRel(0, -50) # move mouse down by 50 pixels
        gui.hold(2)

def movemouseshake(x_list, y_list):
    gui.PAUSE = 0.5 # set pause duration to 0.5 seconds
    for x, y in zip(x_list, y_list):
        gui.moveTo(x, y)
        gui.dragRel(random.randint(-50, 50), random.randint(-50, 50), duration=0.5)

def movemousespray(x_list, y_list):
    for x, y in zip(x_list, y_list):
        angle = math.radians(250) # convert angle to radians
        x_offset = math.cos(angle) * 50 # calculate x offset
        y_offset = math.sin(angle) * 50 # calculate y offset
        gui.moveTo(x + x_offset, y + y_offset)