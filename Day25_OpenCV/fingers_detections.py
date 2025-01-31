# -*- coding: utf-8 -*-
import cv2
import mediapipe as mp
import math

# Inisialisasi modul hands dari MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,  # Maksimal jumlah tangan yang dideteksi
    min_detection_confidence=0.7,  # Minimal confidence untuk deteksi awal
    min_tracking_confidence=0.7  # Minimal confidence untuk tracking
)
mp_drawing = mp.solutions.drawing_utils

# Inisialisasi webcam
cap = cv2.VideoCapture(0)

# Variabel untuk menyimpan posisi sebelumnya
prev_positions = {}


def calculate_distance(point1, point2):
    """Menghitung jarak Euclidean antara dua titik"""
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


# Mengatur jendela menjadi full screen
cv2.namedWindow('Hand Movement Detection', cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty('Hand Movement Detection', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("Gagal membaca frame")
        continue

    # Konversi warna BGR ke RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Proses deteksi tangan
    results = hands.process(image_rgb)

    # Jika tangan terdeteksi
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Gambar landmark tangan di frame
            mp_drawing.draw_landmarks(
                image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Dapatkan koordinat landmark ujung jari telunjuk (ID 8)
            index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            h, w, c = image.shape
            cx, cy = int(index_finger_tip.x * w), int(index_finger_tip.y * h)

            # Simpan posisi saat ini
            current_position = (cx, cy)

            # Deteksi gerakan dengan membandingkan posisi saat ini dan sebelumnya
            if 8 in prev_positions:  # 8 adalah ID untuk ujung jari telunjuk
                prev = prev_positions[8]

                # Hitung jarak pergerakan
                distance = calculate_distance(prev, current_position)

                # Tentukan threshold gerakan (bisa disesuaikan)
                movement_threshold = 30

                if distance > movement_threshold:
                    # Gambar garis dan tampilkan status gerakan
                    cv2.line(image, prev, current_position, (0, 255, 0), 3)
                    cv2.putText(image, 'GERAKAN TERDETEKSI', (10, 50),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            # Update posisi sebelumnya
            prev_positions[8] = current_position

    # Tampilkan frame
    cv2.imshow('Hand Movement Detection', image)

    # Keluar dengan menekan 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Rilis resource
cap.release()
cv2.destroyAllWindows()