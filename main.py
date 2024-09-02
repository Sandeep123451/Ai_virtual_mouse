import cv2
import pyautogui
import mediapipe as mp
from hand_tracking import HandTracker
from gesture_control import GestureControl

def main():
    cap = cv2.VideoCapture(0)  # Start webcam capture
    tracker = HandTracker()  # Initialize hand tracker
    screen_width, screen_height = pyautogui.size()  # Get screen dimensions
    gesture_control = GestureControl(screen_width, screen_height)  # Initialize gesture control

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)  # Flip the frame horizontally
        results = tracker.track_hands(frame)  # Detect hand landmarks
        tracker.draw_hands(frame, results)  # Draw the landmarks on the frame

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                index_finger_tip = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.INDEX_FINGER_TIP]
                thumb_tip = hand_landmarks.landmark[mp.solutions.hands.HandLandmark.THUMB_TIP]

                gesture_control.move_mouse(index_finger_tip)  # Move the mouse
                gesture_control.click(thumb_tip, index_finger_tip)  # Detect click gesture

        cv2.imshow("Virtual Mouse", frame)  # Display the frame
        if cv2.waitKey(1) & 0xFF == ord('q'):  # Exit on pressing 'q'
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
