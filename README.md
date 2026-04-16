# Aerial Object Classification (Bird vs Drone)

##  Overview
This project uses Deep Learning to classify aerial images as **Bird** or **Drone** using MobileNetV2 and Custom CNN.

The project also includes an optional **YOLOv8 object detection approach** for detecting and locating birds or drones using bounding boxes.

##  Features

- Bird vs Drone image classification
- Transfer Learning using MobileNetV2
- Custom CNN model comparison
- Evaluation using Accuracy, Precision, Recall, F1-score
- Confusion Matrix and Training Graphs
- Streamlit web app deployment
- Optional YOLOv8 detection approach

##  Model
- MobileNetV2 (pretrained)
- Achieved high accuracy on test data

##  Evaluation
- Accuracy, Precision, Recall, F1-score
- Confusion Matrix

##  Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py

## Usage

Upload an image → Get prediction (Bird / Drone)

## Tech Stack
Python
TensorFlow/Keras
Streamlit

##  Dataset
Dataset is not included due to size. Please use the provided dataset link.

## Optional YOLOv8 Detection Approach

YOLOv8 can be used as an advanced extension for object detection.

### Steps:
1. Install YOLOv8
2. Use object detection dataset
3. Configure `data.yaml`
4. Train YOLO model
5. Validate performance
6. Run inference
7. Detect Bird/Drone with bounding boxes

## Future Improvements

- Real-time CCTV integration
- Video-based drone detection
- Cloud deployment
- YOLOv8 real-time object detection