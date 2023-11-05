import cv2

# Create a VideoCapture object to access the camera (0 is usually the default camera)
cap = cv2.VideoCapture(0)

# Load the Haar cascade classifier for human detection
human_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open the camera.")
    exit()

# Loop to capture frames from the camera
while True:
    ret, frame = cap.read()  # Read a frame from the camera

    if not ret:
        print("Error: Failed to capture a frame.")
        break

    # Convert the frame to grayscale for human detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect humans in the frame
    humans = human_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around detected humans
    for (x, y, w, h) in humans:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Camera', frame)

    # Exit the loop by pressing the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()