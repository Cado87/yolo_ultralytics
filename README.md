# yolo_ultralytics
Tests using different yolo versions

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
python yolo_tracking.py --source video --model yolo11n --tracker parameters

--source: webcam or video
--model: yolo11n, yolo11n-seg, yolo11n-pose, etc
--tracker: default, parameters, bytetrack or botsort