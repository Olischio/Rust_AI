from roboflow import Roboflow
import cv2 as cv2
import secret

def draw_circles_on_bounding_boxes(image_path, predictions):
    # Get the image dimensions
    image = cv2.imread(image_path)
    height, width, _ = image.shape

    # Loop over the predictions and draw circles on each bounding box
    for prediction in predictions:
        x = prediction['x']
        y = prediction['y']
        w = prediction['width']
        h = prediction['height']

        # Calculate the center coordinates of the bounding box
        cx = x + (w // 20)
        cy = y + (h // 20)

        cx = int(cx)
        cy = int(cy)


        # Draw a circle on the center of the bounding box
        image = cv2.circle(image, (cx, cy), 15, (255, 0, 0), 2)

    # Show the image with circles drawn on each bounding box
    cv2.imshow("Bounding Boxes", image)
    cv2.waitKey(0)

# Create a Roboflow object and get the model predictions
rf = Roboflow(api_key=secret.key)
project = rf.workspace().project("rustirn_mega")
model = project.version(1).model
predictions = model.predict("images/rust.image.elevator.jpg", confidence=40, overlap=30).json()['predictions']
predictionImage = model.predict("images/rust.image.elevator.jpg", confidence=40, overlap=30).save("prediction.jpg")

# Draw circles on each bounding box in the image
draw_circles_on_bounding_boxes("images/rust.image.elevator.jpg", predictions)