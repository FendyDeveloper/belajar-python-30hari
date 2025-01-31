import cv2
import mediapipe as mp
from math import hypot
import screen_brightness_control as sbc
import numpy as np

my_hand = mp.solutions.hands
hands = my_hand.Hands(
    max_num_hands=1,
    min_detection_confidence=0.8,
    min_tracking_confidence=0.8
)
camera = cv2.VideoCapture(0)
mp_drawing = mp.solutions.drawing_utils


while camera.isOpened():
    success, frame = camera.read()
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    lm_list = []
    results = hands.process(image)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, _ = image.shape
                cx = int(lm.x * w)
                cy = int(lm.y * h)

                lm_list.append([id, cx, cy])

            mp_drawing.draw_landmarks(frame, handLms, my_hand.HAND_CONNECTIONS)

    if lm_list != []:
        x1 = lm_list[4][1]
        y1 = lm_list[4][2]
        x2 = lm_list[8][1]
        y2 = lm_list[8][2]
        cv2.circle(frame, (x1, y1), 10, (255, 0, 0), cv2.FILLED)
        cv2.circle(frame, (x2, y2), 10, (255, 0, 0), cv2.FILLED)
        cv2.line(frame, (x1, y1), (x2, y2), (255, 0, 0), 3)
        hypotenuse = hypot(x2 - x1, y2 - y1)
        brightness = np.interp(hypotenuse, [15, 200], [0, 100]) # 200 = 100%, 15 = 0% brightness
        # print(brightness)
        cv2.putText(frame, f'Brightness Active : {int(brightness)}%', (10, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)
        sbc.set_brightness(int(brightness))

    cv2.imshow("Screen Brightness Control", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()








