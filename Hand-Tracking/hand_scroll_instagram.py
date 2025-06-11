import cv2
import mediapipe as mp
import pyautogui
import time

# MediaPipe hand detector
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Parameters scrolling
SCROLL_SENSITIVITY = 20  # Adjust scroll amount sensitivity, smaller value = more sensitive

def main():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Cannot open webcam")
        return

    with mp_hands.Hands(
        max_num_hands=1,
        min_detection_confidence=0.7,
        min_tracking_confidence=0.7) as hands:

        prev_y = None
        scroll_delay = 0.1  # seconds
        last_scroll_time = time.time()

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Flip frame horizontally for natural mirror effect
            frame = cv2.flip(frame, 1)

            # Convert color for MediaPipe
            image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = hands.process(image_rgb)

            height, width, _ = frame.shape

            if results.multi_hand_landmarks:
                hand_landmarks = results.multi_hand_landmarks[0]

                # Draw landmarks
                mp_drawing.draw_landmarks(
                    frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Get the y coordinate of the wrist (landmark 0)
                wrist_y = hand_landmarks.landmark[0].y * height

                if prev_y is not None:
                    diff = wrist_y - prev_y

                    current_time = time.time()
                    if abs(diff) > 5 and (current_time - last_scroll_time) > scroll_delay:
                        if diff > 0:
                            # Hand moved down - scroll down
                            pyautogui.scroll(-SCROLL_SENSITIVITY)
                            # print("Scroll down")
                        else:
                            # Hand moved up - scroll up
                            pyautogui.scroll(SCROLL_SENSITIVITY)
                            # print("Scroll up")

                        last_scroll_time = current_time

                prev_y = wrist_y
            else:
                # No hand detected
                prev_y = None

            # kata kata
            cv2.putText(frame, "Malas aja si", (10,30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

            cv2.imshow("Hand Scroll Instagram", frame)

            key = cv2.waitKey(1)
            if key == 27 or key == ord('q'):
                # Press ESC or q to quit
                break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

