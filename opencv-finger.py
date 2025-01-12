import cv2
import mediapipe as mp
import time

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.5
)
mp_draw = mp.solutions.drawing_utils

# Start video capture
cap = cv2.VideoCapture(0)

# Previous time for FPS calculation
pTime = 0

while True:
    # Read frame from camera
    success, img = cap.read()

    # Convert BGR image to RGB
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Process the image and detect hands
    results = hands.process(imgRGB)

    # If hands are detected, draw landmarks
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Get landmark coordinates
            for id, lm in enumerate(hand_landmarks.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)

                # Draw bigger circles for fingertips (landmarks 4,8,12,16,20)
                if id in [4, 8, 12, 16, 20]:
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

            # Draw hand landmarks and connections
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Calculate and display FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (10, 70),
                cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    # Display the image
    cv2.imshow("Hand Tracking", img)

    # Break loop on 'q' press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()

import numpy as np


def virtual_painter():
    canvas = np.zeros((480, 640, 3), np.uint8)
    draw_color = (255, 0, 0)  # Warna biru default

    while True:
        # ... kode existing ...

        if results.multi_hand_landmarks:
            index_finger = hand_landmarks.landmark[8]
            x, y = int(index_finger.x * w), int(index_finger.y * h)

            # Menggambar saat jari telunjuk terangkat
            middle_finger = hand_landmarks.landmark[12]
            if middle_finger.y > index_finger.y:  # Telunjuk terangkat
                cv2.circle(canvas, (x, y), 5, draw_color, -1)

        # Gabungkan canvas dengan frame asli
        img = cv2.addWeighted(img, 1, canvas, 0.5, 0)
        cv2.imshow("Virtual Painter", img)