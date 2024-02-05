import cv2
import numpy as np
from flask import Flask, request, render_template, Response, jsonify

app = Flask(__name__)

# Set the maximum number of frames to keep in the array
max_frames = 5

# Initialize an empty frame array
frame_array = []

def process_video(file_stream):
    cap = cv2.VideoCapture(file_stream)
    
    frame_count = 0  # Initialize frame count for creating unique filenames

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

        # Yield the frame for the Flask streaming response
        ret, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

        # Save the frame as text to a unique filename
        filename = f'frame_{frame_count}.txt'
        with open(filename, 'a') as f:
            np.savetxt(f, frame.flatten(), fmt='%d', delimiter=',')

        frame_count += 1  # Increment frame count for the next iteration

    # Release the video capture object
    cap.release()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'status': 'error', 'message': 'No file part'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'status': 'error', 'message': 'No selected file'})

    if file:
        # Process the video and return a successful response
        return jsonify({'status': 'ok', 'message': 'Upload successful'})

if __name__ == '__main__':
    app.run(debug=True)
