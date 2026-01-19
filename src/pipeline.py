import cv2
from detection.yolo_detector import YOLODetector
from tracking.kalman_tracker import KalmanTracker

class TrackingPipeline:
    def __init__(self):
        self.detector = YOLODetector()
        self.tracker = KalmanTracker()

    def process_frame(self, frame):
        detections = self.detector.detect(frame)
        for x1, y1, x2, y2 in detections:
            center = ((x1+x2)//2, (y1+y2)//2)
            px, py = self.tracker.update(center)

            cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.circle(frame,(px,py),5,(255,0,0),-1)
        return frame
