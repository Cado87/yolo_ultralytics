# yolo_ultralytics
Tests using different yolo versions
Sources: https://docs.ultralytics.com/modes/track/

Conda environment
web: https://docs.ultralytics.com/guides/conda-quickstart/#prerequisites

First, let's create a new Conda environment. Open your terminal and run the following command:
conda create --name ultralytics-env python=3.11 -y

Activate the new environment:
conda activate ultralytics-env

To see environments created:
conda env list

Execute scripts using python.exe

Script yolo_tracking.py will download a model to models folder and open a window to start tracking


There is the possibility of input parameters:
python yolo_tracking.py --source video --model yolo11n --tracker parameters --conf 0.5

--source: webcam or video
--model: yolo11n, yolo11n-seg, yolo11n-pose, etc
--tracker: default, parameters, bytetrack or botsort
--conf: confidence threshold for detections (0.0-1.0, default: 0.25)

To run script to plot tracking trajectory:
python .\plotting_tracks.py

Image classification:
python image_classification_2.py
Run this script to obtain a classification of the file you input

Convert model to ONNX, run an inference and generate an image with the results:
python onnx_export.py