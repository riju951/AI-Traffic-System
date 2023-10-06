from tracking.centroidtracker import CentroidTracker
from tracking.trackableobject import TrackableObject
from ultralytics import YOLO
# from yolov5.models.experimental import attempt_load
import cv2
import numpy as np
import time
import torch
import os
import dlib

def countVehicles(param):

    # Initialize Ultralytics YOLOv5 model
    img_size = 416
    # weights_path = '/Users/setuparmar/Documents/Adaptive-Traffic-Signal-Control-System-master/yolov5s.pt'  # Replace with the path to your YOLOv5 weights file
    # model = attempt_load(weights_path, map_location=torch.device('cpu'))
    yolo = YOLO("/Users/setuparmar/Documents/Adaptive-Traffic-Signal-Control-System-master/yolov8n.pt")

    ct = CentroidTracker(maxDisappeared=5, maxDistance=50)
    trackers = []
    trackableObjects = {}
    skip_frames = 10
    confidence_level = 0.40
    total = 0
    use_original_video_size_as_output_size = True

    video_path = os.getcwd() + param
    video_name = os.path.basename(video_path)

    all_classes = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck",
                   "boat", "traffic light", "fire hydrant", "stop sign", "parking meter", "bench",
                   "bird", "cat", "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe",
                   "backpack", "umbrella", "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard",
                   "sports ball", "kite", "baseball bat", "baseball glove", "skateboard", "surfboard",
                   "tennis racket", "bottle", "wine glass", "cup", "fork", "knife", "spoon", "bowl", "banana",
                   "apple", "sandwich", "orange", "broccoli", "carrot", "hot dog", "pizza", "donut", "cake",
                   "chair", "sofa", "pottedplant", "bed", "diningtable", "toilet", "tvmonitor", "laptop", "mouse",
                   "remote", "keyboard", "cell phone", "microwave", "oven", "toaster", "sink", "refrigerator",
                   "book", "clock", "vase", "scissors", "teddy bear", "hair drier", "toothbrush"]

    classes = {1: 'bicycle', 2: 'car', 3: 'motorbike', 5: 'bus', 7: 'truck'}

    cap = cv2.VideoCapture(video_path)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    width_scale = 1
    height_scale = 1

    if use_original_video_size_as_output_size:
        width_scale = width / img_size
        height_scale = height / img_size
        
    skipped_frames_counter = 0
    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break

        img = cv2.resize(frame, (img_size, img_size))
        output_img = frame if use_original_video_size_as_output_size else img

        tracker_rects = []

        if skipped_frames_counter == skip_frames:
            trackers = []
            

            results = yolo(img)
            #print(results)
            for result in results.pred[0]:
                class_index = int(result[5])
                class_name = all_classes[class_index]

                if class_index in classes.keys() and result[4] >= confidence_level:
                    local_count += 1
                    startX, startY, endX, endY = result[:4].astype(int)

                    cv2.rectangle(output_img, (startX, startY), (endX, endY), (0, 255, 0), 1)
                    cv2.putText(output_img, class_name, (startX, startY), cv2.FONT_HERSHEY_SIMPLEX, .5, (0, 0, 255), 1)

                    tracker = dlib.correlation_tracker()
                    rect = dlib.rectangle(startX, startY, endX, endY)
                    tracker.start_track(img, rect)
                    trackers.append(tracker)
        else:
            # ...
            cv2.imshow(video_name, img)
            save_path = '/Users/setuparmar/Documents/Adaptive-Traffic-Signal-Control-System-master/images/image.jpg'
        # Save the image using cv2.imwrite
            cv2.imwrite(save_path, img)
            # Rest of your code (tracking, counting, and displaying)
            pass           
        
                    

                    
        

    cap.release()
    cv2.destroyAllWindows()
    # print("Exited")

if __name__ == "__main__":
    countVehicles("/videos/test.mp4")
