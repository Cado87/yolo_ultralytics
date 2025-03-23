from ultralytics import YOLO

# Load an official or custom model
model = YOLO("models/yolov8m.pt")  # Load an official Detect model

# Perform tracking with the model
results = model.track(source=0, show=True, tracker='bytetrack.yaml')