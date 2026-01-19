import cv2
from pipeline import TrackingPipeline

pipeline = TrackingPipeline()

cap1 = cv2.VideoCapture("data/video1.mp4")
cap2 = cv2.VideoCapture("data/video2.mp4")

while cap1.isOpened() and cap2.isOpened():
    ret1, f1 = cap1.read()
    ret2, f2 = cap2.read()
    if not ret1 or not ret2:
        break

    out1 = pipeline.process_frame(f1)
    out2 = pipeline.process_frame(f2)

    cv2.imshow("Camera 1", out1)
    cv2.imshow("Camera 2", out2)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap1.release()
cap2.release()
cv2.destroyAllWindows()
