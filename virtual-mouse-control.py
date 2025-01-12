import cv2
import mediapipe as mp
import numpy as np
import pygame
from math import hypot
import time


class HandGestureController:
    def __init__(self):
        # Inisialisasi MediaPipe
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=2,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.5
        )
        self.mp_draw = mp.solutions.drawing_utils

        # Inisialisasi kamera
        self.cap = cv2.VideoCapture(0)

        # Mode program (0: Finger Detection, 1: Virtual Painter, 2: Air Piano)
        self.mode = 0

        # Virtual Painter variables
        self.canvas = None
        self.draw_color = (255, 0, 0)  # Warna default: Biru
        self.brush_thickness = 15
        self.prev_point = None

        # Air Piano variables
        pygame.mixer.init()
        self.notes = {
            'C': pygame.mixer.Sound('piano_sounds/C.wav') if self._check_sound_file('piano_sounds/C.wav') else None,
            'D': pygame.mixer.Sound('piano_sounds/D.wav') if self._check_sound_file('piano_sounds/D.wav') else None,
            'E': pygame.mixer.Sound('piano_sounds/E.wav') if self._check_sound_file('piano_sounds/E.wav') else None,
            'F': pygame.mixer.Sound('piano_sounds/F.wav') if self._check_sound_file('piano_sounds/F.wav') else None,
        }
        self.note_regions = [(0, 150), (150, 300), (300, 450), (450, 600)]
        self.last_played = time.time()
        self.play_delay = 0.3  # Delay antara nada (dalam detik)

    def _check_sound_file(self, file_path):
        try:
            open(file_path)
            return True
        except FileNotFoundError:
            print(f"Warning: Sound file {file_path} not found")
            return False

    def detect_fingers(self, hand_landmarks):
        fingers = []
        # Thumb
        if hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_TIP].x < \
                hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_IP].x:
            fingers.append(1)
        else:
            fingers.append(0)

        # 4 Fingers
        for tip_id in [8, 12, 16, 20]:  # Index, Middle, Ring, Pinky tips
            if hand_landmarks.landmark[tip_id].y < hand_landmarks.landmark[tip_id - 2].y:
                fingers.append(1)
            else:
                fingers.append(0)
        return fingers

    def virtual_painter(self, frame, hand_landmarks):
        if self.canvas is None:
            self.canvas = np.zeros_like(frame)

        # Get index finger tip position
        index_finger = hand_landmarks.landmark[8]
        h, w, _ = frame.shape
        x, y = int(index_finger.x * w), int(index_finger.y * h)

        # Check if middle finger is up (for drawing mode)
        middle_finger = hand_landmarks.landmark[12]
        drawing_mode = middle_finger.y > index_finger.y

        if drawing_mode:
            if self.prev_point:
                cv2.line(self.canvas, self.prev_point, (x, y), self.draw_color, self.brush_thickness)
            self.prev_point = (x, y)
        else:
            self.prev_point = None

        # Combine the canvas with the original frame
        frame = cv2.addWeighted(frame, 1, self.canvas, 0.5, 0)
        return frame

    def air_piano(self, frame, hand_landmarks):
        h, w, _ = frame.shape

        # Draw piano regions
        for i, (start, end) in enumerate(self.note_regions):
            cv2.rectangle(frame, (start, 100), (end, 400), (255, 0, 0), 2)
            cv2.putText(frame, list(self.notes.keys())[i], (start + 60, 380),
                        cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        # Get index finger tip position
        index_finger = hand_landmarks.landmark[8]
        x, y = int(index_finger.x * w), int(index_finger.y * h)

        # Check if finger is in piano region
        if 100 < y < 400:
            for i, (start, end) in enumerate(self.note_regions):
                if start < x < end:
                    current_time = time.time()
                    if current_time - self.last_played > self.play_delay:
                        note = list(self.notes.keys())[i]
                        if self.notes[note]:
                            self.notes[note].play()
                            self.last_played = current_time
                            cv2.circle(frame, (x, y), 20, (0, 255, 0), -1)

        return frame

    def run(self):
        while True:
            success, frame = self.cap.read()
            if not success:
                break

            # Flip the frame horizontally for a later selfie-view display
            frame = cv2.flip(frame, 1)

            # Convert to RGB
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = self.hands.process(rgb_frame)

            # Display mode text
            mode_text = ["Finger Detection", "Virtual Painter", "Air Piano"][self.mode]
            cv2.putText(frame, f"Mode: {mode_text}", (10, 30),
                        cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 2)
            cv2.putText(frame, "Press 0-2 to change mode", (10, 60),
                        cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 2)

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    # Draw hand landmarks
                    self.mp_draw.draw_landmarks(frame, hand_landmarks,
                                                self.mp_hands.HAND_CONNECTIONS)

                    if self.mode == 0:  # Finger Detection
                        fingers = self.detect_fingers(hand_landmarks)
                        finger_text = f"Fingers up: {sum(fingers)}"
                        cv2.putText(frame, finger_text, (10, 90),
                                    cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 2)

                    elif self.mode == 1:  # Virtual Painter
                        frame = self.virtual_painter(frame, hand_landmarks)

                    elif self.mode == 2:  # Air Piano
                        frame = self.air_piano(frame, hand_landmarks)

            cv2.imshow("Hand Gesture Controller", frame)

            # Handle keyboard input
            key = cv2.waitKey(1)
            if key == ord('q'):
                break
            elif key in [ord('0'), ord('1'), ord('2')]:
                self.mode = int(chr(key))
            elif key == ord('c') and self.mode == 1:  # Clear canvas in Virtual Painter mode
                self.canvas = None

        self.cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    controller = HandGestureController()
    controller.run()