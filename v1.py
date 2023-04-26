from roboflow import Roboflow
import cv2 as cv2
import secret

rf = Roboflow(api_key=secret.key)
project = rf.workspace().project("rustirn_mega")
model = project.version(1).model

# infer on a local image
prediction = (model.predict("images/bilde2.jpg", confidence=10, overlap=0).json())
print(prediction)

# infer on an image hosted elsewhere
# print(model.predict("URL_OF_YOUR_IMAGE", hosted=True, confidence=40, overlap=30).json())

# visualize your prediction
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


        # Draw a circle on the center of the bounding box
        image = cv2.circle(image, (cx, cy), 15, (255, 0, 0), 2)

    # Show the image with circles drawn on each bounding box

    cv2.imshow("Bounding Boxes", image)
    cv2.waitKey(0)

draw_circles_on_bounding_boxes("images/bilde2.jpg", predictions)



#Gamle koden fra før jeg lagde det om til en loop

# path = "C:\\Users\\Oliver S\\OneDrive - Osloskolen\\Desktop\\RustAI\\prediction.jpg"
# center_coordinates = []
# window_name = "Prikk"

# x = preds_x[0]
# y = preds_y[0]
# X = x + (width[0] // 20)
# Y = y + (height[0] // 20)

# center_coordinates.append((int(X),int(Y)))

# image = cv2.imread(path)
# image = cv2.circle(image, center_coordinates[0], 15, (255,0,0), 2)

# cv2.imshow("Sirkel I BoundingBox", image)
# cv2.waitKey(0)