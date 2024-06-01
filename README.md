
# Face Recognition with OpenCV and Face Recognition Library

This project uses OpenCV and the Face Recognition library to perform real-time face recognition using a webcam. The implementation captures video frames from the webcam, detects faces, and identifies them based on a predefined set of known faces.

## Requirements

To run this project, you need to have the following libraries installed:

- `numpy`
- `face_recognition`
- `opencv-python`

You can install them using pip:

```sh
pip install numpy face_recognition opencv-python
```

## Project Structure

- `face_recognition.py`: The main script that runs the face recognition.
- `isma.jpg`: An example image used for face encoding. Replace this with your own image.

## How It Works

1. **Video Capture**: The script starts capturing video from the default webcam.
2. **Face Encoding**: It loads a predefined image (`isma.jpg` in this case) and creates an encoding for this face.
3. **Face Detection and Recognition**: For each frame captured from the webcam, the script:
   - Converts the frame from BGR (used by OpenCV) to RGB.
   - Detects faces in the frame.
   - Compares the detected faces with the known faces.
   - Draws rectangles around the faces and labels them with the recognized names.
4. **Display**: The processed frames are displayed in a window.
5. **Exit**: The loop continues until the user presses the 'q' key, after which the video capture is released and all windows are closed.

## Usage

1. **Prepare Known Faces**:
   - Replace `isma.jpg` with your own image files and update the script accordingly to include your own face encodings and names.

2. **Run the Script**:
   - Ensure your webcam is connected and functional.
   - Execute the script:

   ```sh
   python face_recognition.py
   ```

3. **Exit**:
   - Press 'q' to stop the video capture and close all windows.


## Notes

- Ensure your webcam drivers are installed and the device is working correctly.
- This script uses a single known face (`isma.jpg`) (is not there but it is an example). To add more known faces, load additional images, encode them, and append their encodings and names to `facceNote` and `nomiFacceNote`.

## Troubleshooting

- If the webcam is not detected, check if the device is connected and recognized by your operating system.
- Ensure the face image used for encoding is clear and well-lit for accurate recognition.

## Contributing

We welcome contributions to this project! If you have any improvements, bug fixes, or new features, please feel free to submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.
