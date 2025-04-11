import cv2
import mediapipe as mp
import pygame
import time
import os
import numpy as np
from scipy.spatial import distance
from ultralytics import YOLO

# ------------------------ Setup ------------------------
# Load YOLOv8 for phone detection
model = YOLO('yolov8n.pt')
# Mediapipe for face mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()

# Initialize beep sound
pygame.init()
pygame.mixer.init()
beep_path = os.path.abspath("alert.mp3")
pygame.mixer.music.load(beep_path)

# EAR calculation
def eye_aspect_ratio(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    return (A + B) / (2.0 * C)

# ------------------------ Constants ------------------------
EAR_THRESHOLD = 0.25
EYE_CLOSE_FRAMES = 15
eye_closed_counter = 0
buzzing = False

# Eye landmarks
LEFT_EYE = [362, 385, 387, 263, 373, 380]
RIGHT_EYE = [33, 160, 158, 133, 153, 144]

# ------------------------ Webcam Start ------------------------
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    h, w, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = face_mesh.process(rgb_frame)

    # 1. Phone Detection
    phone_detected = False
    results = model.predict(source=frame, imgsz=320, conf=0.4, verbose=False)
    for box in results[0].boxes:
        cls = int(box.cls[0])
        label = model.names[cls]
        if label == 'cell phone':
            phone_detected = True
            break

    # 2. Eye Closure Detection
    eyes_closed = False
    if result.multi_face_landmarks:
        for landmarks in result.multi_face_landmarks:
            landmark_points = landmarks.landmark
            left_eye = [(int(landmark_points[i].x * w), int(landmark_points[i].y * h)) for i in LEFT_EYE]
            right_eye = [(int(landmark_points[i].x * w), int(landmark_points[i].y * h)) for i in RIGHT_EYE]
            left_ear = eye_aspect_ratio(left_eye)
            right_ear = eye_aspect_ratio(right_eye)
            avg_ear = (left_ear + right_ear) / 2.0

            if avg_ear < EAR_THRESHOLD:
                eye_closed_counter += 1
            else:
                eye_closed_counter = 0

            if eye_closed_counter >= EYE_CLOSE_FRAMES:
                eyes_closed = True

    # 3. Trigger Buzzer if either condition is True
    if (phone_detected or eyes_closed):
        if not buzzing:
            pygame.mixer.music.play()
            buzzing = True
            print("🔊 Buzzing - Phone or Eyes Closed!")
    else:
        if buzzing:
            pygame.mixer.music.stop()
            buzzing = False

    # Display info
    status_text = f"Phone: {'Yes' if phone_detected else 'No'} | Eyes Closed: {'Yes' if eyes_closed else 'No'}"
    cv2.putText(frame, status_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    cv2.imshow("Driver Safety Monitor", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC key
        break

cap.release()
cv2.destroyAllWindows()
