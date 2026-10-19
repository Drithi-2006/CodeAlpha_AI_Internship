from ultralytics import YOLO
import cv2
from collections import Counter

# Load YOLO model
model = YOLO("yolo11n.pt")

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Could not access camera")
        break

    # Detect and track objects
    results = model.track(frame, persist=True)

    # Draw boxes and tracking IDs
    annotated_frame = results[0].plot()

    # Count detected objects
    if results[0].boxes.cls is not None:
        class_ids = results[0].boxes.cls.cpu().numpy().astype(int)
        names = results[0].names

        object_names = [names[class_id] for class_id in class_ids]
        counts = Counter(object_names)

        # Display object counts
        y_position = 30

        for name, count in counts.items():
            text = f"{name}: {count}"
            cv2.putText(
                annotated_frame,
                text,
                (10, y_position),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2
            )
            y_position += 30

    cv2.imshow("YOLO Object Detection and Tracking", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()