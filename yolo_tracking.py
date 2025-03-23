from ultralytics import YOLO
import tkinter as tk
from tkinter import filedialog

# Load an official or custom model
#model = YOLO("models/yolov8m.pt")
model = YOLO("models/yolo11n.pt") # Load an official Detect model
#model = YOLO("models/yolo11n-seg.pt")  # Load an official Segment model
#model = YOLO("models/yolo11n-pose.pt")  # Load an official Pose model

# Perform tracking with the model

# Webcam
#results = model.track(source=0, show=True)  # Tracking with default tracker
#results = model.track(source=0, show=True, tracker='tracker_config/bytetrack.yaml') # with ByteTrack
#results = model.track(source=0, show=True, tracker='tracker_config/botsort.yaml') # with BoT-SORT

#Video
# Ask the user for the video file path using a file dialog
root = tk.Tk()
root.withdraw()  # Hide the root window
video_path = filedialog.askopenfilename(title="Select the video file", filetypes=[("Video files", "*.mp4;*.avi;*.mov")])

#results = model.track(video_path, show=True)  # Tracking with default tracker
results = model.track(video_path, conf=0.3, iou=0.5, show=True)  # Tracking with confidence and IoU threshold
#results = model.track(video_path, show=True, tracker='tracker_config/bytetrack.yaml')  # with ByteTrack
#results = model.track(video_path, show=True, tracker='tracker_config/botsort.yaml')  # with BoT-SORT
