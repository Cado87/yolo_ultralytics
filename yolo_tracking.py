from ultralytics import YOLO

# Load an official or custom model
#model = YOLO("models/yolov8m.pt")
model = YOLO("models/yolo11n.pt") # Load an official Detect model
#model = YOLO("models/yolo11n-seg.pt")  # Load an official Segment model
#model = YOLO("models/yolo11n-pose.pt")  # Load an official Pose model

# Perform tracking with the model
#results = model.track(source=0, show=True)  # Tracking with default tracker
results = model.track(source=0, show=True, tracker='tracker_config/bytetrack.yaml') # with ByteTrack
#results = model.track(source=0, show=True, tracker='tracker_config/botsort.yaml') # with BotSort
