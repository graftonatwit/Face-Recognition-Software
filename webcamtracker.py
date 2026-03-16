import face_recognition
import cv2

# Load your face image and encode it
my_image = face_recognition.load_image_file("static/my_face.jpg")
my_face_encoding = face_recognition.face_encodings(my_image)[0]

# Create arrays of known face encodings and their names
known_face_encodings = [my_face_encoding]
known_face_names = ["Trevor"]

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    # Convert the frame from BGR (OpenCV) to RGB (face_recognition)
    rgb_frame = frame[:, :, ::-1]
    
    # Find all face locations and face encodings in the current frame
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
    
    for face_encoding, face_location in zip(face_encodings, face_locations):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        
        name = "Unknown"
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]
            print(f"{name} detected!")  # Terminal prints when your face is recognized
        
        # Optional: draw rectangle and label
        top, right, bottom, left = face_location
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    
    cv2.imshow("Face Recognition", frame)
    
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
