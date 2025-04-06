from ultralytics import YOLO

#Train YOLO11n on the COCO8 dataset for 10 epochs at image size 640. The training device can be specified using the device argument.
#If no argument is passed GPU device=0 will be used if available, otherwise device='cpu' will be used. 


# Load a model
model = YOLO("yolo11n.yaml")  # build a new model from YAML
model = YOLO("models/yolo11n.pt")  # load a pretrained model (recommended for training)
model = YOLO("yolo11n.yaml").load("models/yolo11n.pt")  # build from YAML and transfer weights

# Train the model
results = model.train(data="coco8.yaml", epochs=10, imgsz=640)