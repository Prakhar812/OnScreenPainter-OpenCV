import cv2
import mediapipe as mp

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Set up webcam capture
cap = cv2.VideoCapture(0)

# Use MediaPipe Hands model
with mp_hands.Hands(
    static_image_mode=False,       # False for real-time
    max_num_hands=3,               # Detect up to 2 hands
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
) as hands:
    
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            continue

        # Flip the frame horizontally for mirror effect
        frame = cv2.flip(frame, 1)

        # Convert to RGB (MediaPipe needs RGB images)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the frame
        results = hands.process(rgb_frame)

        # Draw hand landmarks
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    frame,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS
                )

        # Display
        cv2.imshow('Hand Tracking', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):  # ESC to exit
            break

cap.release()
cv2.destroyAllWindows()
