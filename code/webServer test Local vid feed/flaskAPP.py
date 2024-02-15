import cv2
import numpy as np
from flask import Flask, render_template, Response, jsonify, request

app = Flask(__name__)

# Set the maximum number of frames to keep in the array
max_frames = 5

# Initialize an empty frame array
frame_array = []

def process_video(file_stream):
    cap = cv2.VideoCapture(file_stream)

    while True:
        # Read a frame from the video
        ret, frame = cap.read()

        if not ret:
            print("End of video.")
            break

        # Append the new frame to the array
        frame_array.append(frame)

        # Yield the frame for the Flask streaming response
        ret, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

    # Release the video capture object
    cap.release()

def generate_preview_frames():
    while True:
        if len(frame_array) > 0:
            latest_frame = frame_array[-1]
            print("Latest frame shape:", latest_frame.shape)
            ret, buffer = cv2.imencode('.jpg', latest_frame)
            frame_bytes = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')


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

@app.route('/preview')
def preview():
    return render_template('preview.html', preview_route="/preview")


if __name__ == '__main__':
    app.run(debug=True)
