from roboflow import Roboflow
import cv2 as cv2
import os
import secret
import Functions

def Run():

    rf = Roboflow(api_key="x")
    project = rf.workspace().project("rustirn_mega")
    model = project.version(1).model

    pathToImagesFolder = "C:\\Users\\Oliver S\\OneDrive - Osloskolen\\Desktop\\RustAI"
    for filename in os.listdir("screenshot"):
        img = cv2.imread(os.path.join("screenshot", filename))
        if img is not None:

            prediction = (model.predict(os.path.join("screenshot", filename), confidence=10, overlap=0).json())
            print(prediction)

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

            image_path = "C:\\Users\\Oliver S\\OneDrive - Osloskolen\\Desktop\\RustAI\\prediction.jpg"

            def draw_circles_on_bounding_boxes(image_path, predictions):
                # Get the image dimensions
                image = cv2.imread(image_path)

                #Få størrelse på bilde
                # imgwidth = int(image.shape[1])
                # imgheight = int(image.shape[0])

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

                    Circle_Coordinates = []
                    Circle_Coordinates.append(cx)
                    Circle_Coordinates.append(cy)


                    image = cv2.circle(image, (cx, cy), 15, (255, 0, 0), 2)

                cv2.imshow("Bounding Boxes", image)
                cv2.waitKey(0)

                return Circle_Coordinates

            open("screenshot\\prediction.jpg", "w+").close()
            draw_circles_on_bounding_boxes(os.path.join("screenshot", filename), predictions)

