File name: README_FaceRecognition.md

# Face Recognition Login System

## Overview
This is a standalone **face recognition login system** built using Python. It allows a user to authenticate via their webcam using the `face_recognition` library. The system captures a live image from the camera, compares it against a known face, and confirms login if a match is found.

This project can be used as a security/login module for applications or demonstrations of face-based authentication.

---

## Features
- Uses the **user’s webcam** to capture live images.
- Compares captured images to a **known face image** using the `face_recognition` Python library.
- Returns **authentication success or failure**.
- Can be integrated with web apps, desktop apps, or other systems requiring login verification.
- Provides optional messaging and can be extended to auto-redirect after successful authentication.

---

## Technologies Used
- Python 3.x
- `face_recognition` library
- `opencv-python` (`cv2`) for camera capture
- `numpy` (dependency of face_recognition)
- PIL (used by face_recognition internally)

---

## Installation

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd face_recognition_login

Install dependencies

pip install face_recognition opencv-python numpy Pillow

Add your known face image

Place a file like my_face.jpg in the project folder.

This image will be used as the reference for recognition.

Usage

Run the script

python face_auth.py

Allow camera access

The webcam will open in a window, showing the live feed.

Authentication

Position your face in front of the camera.

If the face matches the known face, the script will print:

Face recognized! Login successful.

If no match is found, the script will continue scanning until the window is closed.

Exit

Press Esc to close the camera feed and terminate the program.



Future Improvements

Multi-user face authentication

Integration with web applications (e.g., Flask)

Automatic logging of login attempts

GUI enhancements for better user experience

Add email or database verification after successful login

Author

Trevor Grafton
