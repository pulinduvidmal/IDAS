import ast
import numpy as np
import cv2

# Read the frame array from the file
with open('frame_array.txt', 'r') as file:
    frame_array_str = file.readlines()

# Convert the string representations of frames back to NumPy arrays
frame_array = [np.array(ast.literal_eval(frame_str.strip())) for frame_str in frame_array_str]

# Display or use the decoded frames as needed
for frame in frame_array:
    cv2.imshow('Decoded Frame', frame)
    cv2.waitKey(30)

# Close OpenCV windows
cv2.destroyAllWindows()
