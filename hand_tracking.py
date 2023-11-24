import csv
import argparse
import cv2
import mediapipe as mp
from model import keypointclassifier
from model import pointhistoryclassifier

def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("--device", type=int, default=0)
    parser.add_argument("--width", help='cap width', type=int, default=960)
    parser.add_argument("--height", help='cap height', type=int, default=960)

    parser.add_argument("--use_static_image_mode", action='store_true')
    parser.add_argument("--min_detection_confidence",
                        help='min_detection_confidence',
                        type=float, default=0.7)

    parser.add_argument("--min_tracking_confidence",
                        help='min_tracking_confidence',
                        type=int, default=0.5)

    args = parser.parse_args()
    return args

def main():
    args = get_args()

    cap = cv2.VideoCapture(args.device)
    cap.set(3, args.width)
    cap.set(4, args.height)

    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(
        static_image_mode=args.use_static_image_mode,
        max_num_hands=1,
        min_detection_confidence=args.min_detection_confidence,
        min_tracking_confidence=args.min_tracking_confidence
    )

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            continue

        # BGR to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Flip the image horizontally for a later selfie-view display
        rgb_frame = cv2.flip(rgb_frame, 1)

        # Set flag
        results = hands.process(rgb_frame)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Extract hand landmarks and process them as needed
                # You can use hand_landmarks to capture hand gestures

                # Display the resulting frame
                cv2.imshow('Hand Gestures', frame)

                if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
                    break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
