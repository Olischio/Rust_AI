from roboflow import Roboflow
import cv2 as cv2
import os
import secret

rf = Roboflow(api_key=secret.key)
project = rf.workspace().project("rustirn_mega")
model = project.version(1).model

# prediction = (model.predict("images/bilde2.jpg", confidence=10, overlap=0).json())
# print(prediction)

pathToImagesFolder = "C:\\Users\\Oliver S\\OneDrive - Osloskolen\\Desktop\\RustAI"

for filename in os.listdir(pathToImagesFolder):
    img = cv2.imread(os.path.join(pathToImagesFolder, filename))
    if img is not None:

        prediction = (model.predict(os.path.join("images", filename), confidence=10, overlap=0).json())

        predictionImage = model.predict("images/bilde2.jpg", confidence=10, overlap=0).save("prediction.jpg")


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

        print("Coordinates", "x", preds_x, "y", preds_y, "Height & Width", height, width)

        #image_path = "C:\\Users\\Oliver S\\OneDrive - Osloskolen\\Desktop\\RustAI\\prediction.jpg"

        def draw_circles_on_bounding_boxes(image_path, predictions):
           
            image = cv2.imread(image_path)

            for prediction in predictions:
                x = prediction['x']
                y = prediction['y']
                w = prediction['width']
                h = prediction['height']

                cx = x + (w // 20)
                cy = y + (h // -7)

                cx = int(cx)
                cy = int(cy)

                image = cv2.circle(image, (cx, cy), 15, (255, 0, 0), 2)

            cv2.imshow("Bounding Boxes", image)
            cv2.waitKey(0)

        draw_circles_on_bounding_boxes(os.path.join("images", filename), predictions)