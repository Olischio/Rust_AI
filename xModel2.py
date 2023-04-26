from roboflow import Roboflow
import cv2 as cv2
import os
import secret
import xFunctions as x

rf = Roboflow(api_key=secret.key)
project = rf.workspace().project("rustirn_mega")
model = project.version(1).model

# pathToImagesFolder = "C:\\Users\\Oliver S\\OneDrive - Osloskolen\\Desktop\\RustAI"


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
        x.draw_circles_on_bounding_boxes(os.path.join("screenshot", filename), predictions)