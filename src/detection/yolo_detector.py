import torch
import cv2

class YOLODetector:
    def __init__(self):
        self.model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

    def detect(self, frame):
        results = self.model(frame)
        detections = []
        for *box, conf, cls in results.xyxy[0]:
            x1, y1, x2, y2 = map(int, box)
            detections.append((x1, y1, x2, y2))
        return detections
