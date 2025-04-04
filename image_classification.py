from ultralytics import YOLO
import tkinter as tk
from tkinter import filedialog

# Load a model
model = YOLO("models/yolo11n-cls.pt")  # load an official model
#model = YOLO("path/to/best.pt")  # load a custom model

# Ask the user for the image file path using a file dialog
root = tk.Tk()
root.withdraw()  # Hide the root window
image_path = filedialog.askopenfilename(title="Select the image file", filetypes=[("Image files", "*.jpg;*.png;*.jpeg")])

# Predict with the model
results = model(image_path)  # predict on an image