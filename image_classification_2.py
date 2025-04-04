from ultralytics import YOLO
import tkinter as tk
from tkinter import filedialog

# Load a model
model = YOLO("models/yolo11n.pt")  # pretrained YOLO11n model

# Ask the user for the image file path using a file dialog
root = tk.Tk()
root.withdraw()  # Hide the root window
image_path = filedialog.askopenfilename(title="Select the image file", filetypes=[("Image files", "*.jpg;*.png;*.jpeg")])

# Run batched inference on a list of images
results = model(image_path)  # return a list of Results objects

# Process results list
for result in results:
    boxes = result.boxes  # Boxes object for bounding box outputs
    masks = result.masks  # Masks object for segmentation masks outputs
    keypoints = result.keypoints  # Keypoints object for pose outputs
    probs = result.probs  # Probs object for classification outputs
    obb = result.obb  # Oriented boxes object for OBB outputs
    result.show()  # display to screen
    result.save(filename="result.jpg")  # save to disk