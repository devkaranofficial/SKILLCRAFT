import cv2
import mediapipe as mp

# -----------------------------
# MediaPipe Initialization
# -----------------------------
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

# Fingertips
tip_ids = [4, 8, 12, 16, 20]

# Webcam
cap = cv2.VideoCapture(0)

while True:

    success, frame = cap.read()

    if not success:
        break

    frame = cv2.flip(frame, 1)

    h, w, c = frame.shape

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(rgb)

    if results.multi_hand_landmarks:

        for hand_landmarks, hand_info in zip(
                results.multi_hand_landmarks,
                results.multi_handedness):

            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

            landmarks = []

            for lm in hand_landmarks.landmark:

                landmarks.append(
                    (
                        int(lm.x * w),
                        int(lm.y * h)
                    )
                )

            label = hand_info.classification[0].label

            fingers = []

            # --------------------
            # Thumb
            # --------------------
            if label == "Right":

                if landmarks[4][0] < landmarks[3][0]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            else:

                if landmarks[4][0] > landmarks[3][0]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            # --------------------
            # Other Fingers
            # --------------------
            for tip in [8, 12, 16, 20]:

                if landmarks[tip][1] < landmarks[tip - 2][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            total = fingers.count(1)

            # --------------------
            # Gesture Recognition
            # --------------------

            gesture = "Unknown"

            if fingers == [0,0,0,0,0]:
                gesture = "Fist"

            elif fingers == [1,1,1,1,1]:
                gesture = "Open Palm"

            elif fingers == [0,1,0,0,0]:
                gesture = "One Finger"

            elif fingers == [0,1,1,0,0]:
                gesture = "Victory"

            elif fingers == [0,1,1,1,0]:
                gesture = "Three Fingers"

            elif fingers == [1,0,0,0,0]:
                gesture = "Thumbs Up"

            # --------------------
            # Draw Fingertips
            # --------------------

            for tip in tip_ids:

                cx, cy = landmarks[tip]

                cv2.circle(
                    frame,
                    (cx, cy),
                    10,
                    (0, 0, 255),
                    cv2.FILLED
                )

            # --------------------
            # Draw Gesture
            # --------------------

            cv2.rectangle(
                frame,
                (10, 10),
                (320, 90),
                (0, 255, 0),
                -1
            )

            cv2.putText(
                frame,
                "Gesture: " + gesture,
                (20, 60),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 0),
                3
            )

            cv2.putText(
                frame,
                "Hand: " + label,
                (20, 100),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (255,255,255),
                2
            )

    cv2.imshow("SkillCraft Task 04 - Hand Gesture Recognition", frame)

    key = cv2.waitKey(1)

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()