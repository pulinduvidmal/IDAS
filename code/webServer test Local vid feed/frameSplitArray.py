import cv2
import numpy as np

# Set the maximum number of frames to keep in the array
max_frames = 5

# Open a video file or capture from a camera (change the argument accordingly)
cap = cv2.VideoCapture('your_video_file.mp4')

# Initialize an empty frame array
frame_array = []

while True:
    # Read a frame from the video
    ret, frame = cap.read()

    if not ret:
        print("End of video.")
        break

    # Append the new frame to the array
    frame_array.append(frame)

    # If the number of frames exceeds the maximum allowed, remove the oldest frame
    if len(frame_array) > max_frames:
        frame_array.pop(0)

    # Write the frame array to a file after each frame is added
    with open('frame_array.txt', 'w') as file:
        for f in frame_array:
            file.write(str(f.tolist()) + '\n')

    # Display the current frame
    cv2.imshow('Frame', frame)

    # Press 'q' to exit the loop
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# Release the video capture object
cap.release()

# Destroy all OpenCV windows
cv2.destroyAllWindows()
