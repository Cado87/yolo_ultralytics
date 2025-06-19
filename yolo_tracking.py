from ultralytics import YOLO
import tkinter as tk
from tkinter import filedialog
import argparse
import os
import sys  # Import sys for exiting the script

# Parse command-line arguments
parser = argparse.ArgumentParser(description="YOLO Tracking Script")
parser.add_argument("--source", type=str, choices=["webcam", "video"], required=True,
                    help="Choose the source: 'webcam' for webcam or 'video' for a video file")
parser.add_argument("--model", type=str, required=True,
                    help="Path to the YOLO model file (e.g., yolov8m, yolo11n, yolo11n-seg, yolo11n-pose')")
parser.add_argument("--tracker", type=str, choices=["default", "parameters", "bytetrack", "botsort"], default="default",
                    help="Choose the tracker: 'default', 'parameters', 'bytetrack', or 'botsort'")
args = parser.parse_args()


# Construct the full model path
model_path = os.path.join("models", f"{args.model}.pt")

# Load the specified model
try:
    model = YOLO(model_path)
    print(f"Model '{model_path}' loaded successfully.")
except Exception as e:
    print(f"Error loading model '{model_path}': {e}")
    sys.exit(1)


if args.source == "webcam":
    # Perform tracking with the webcam
    if args.tracker == "default":
        results = model.track(source=0, show=True)
    elif args.tracker == "bytetrack":
        results = model.track(source=0, show=True, tracker='tracker_config/bytetrack.yaml')
    elif args.tracker == "botsort":
        results = model.track(source=0, show=True, tracker='tracker_config/botsort.yaml')
    else:
        results = model.track(source=0, show=True)


elif args.source == "video":
    # Ask the user for the video file path using a file dialog
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    video_path = filedialog.askopenfilename(title="Select the video file", filetypes=[("Video files", "*.mp4;*.avi;*.mov")])

    if video_path:
        # Perform tracking with the video file
        if args.tracker == "default":
            results = model.track(video_path, show=True)  # Tracking with default tracker
        elif args.tracker == "parameters":
            results = model.track(video_path, conf=0.3, iou=0.5, show=True)  # Tracking with confidence and IoU threshold
        elif args.tracker == "bytetrack":
            results = model.track(video_path, show=True, tracker='tracker_config/bytetrack.yaml')  # with ByteTrack
        elif args.tracker == "botsort":
            results = model.track(video_path, show=True, tracker='tracker_config/botsort.yaml')  # with BoT-SORT
    else:
        print("No video file selected. Exiting.")

else:
    print("Invalid source. Please choose 'webcam' or 'video'.")
    sys.exit(1)
