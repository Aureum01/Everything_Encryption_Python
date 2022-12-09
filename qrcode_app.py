import cv2
import pyqrcode

# Use OpenCV to capture video from the default camera
cap = cv2.VideoCapture(0)

# Loop indefinitely
while True:
    # Read a frame from the camera
    _, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Use OpenCV to detect QR codes in the frame
    qr_codes = cv2.QRCodeDetector().detect(gray)

    # If any QR codes were detected
    if qr_codes[0] != False:
        # Get the data from the QR code
        data = qr_codes[1]

        # Use PyQRCode to parse the data
        qr = pyqrcode.create(data)

        # Print the data to the console
        print(qr.data)

    # Show the frame in a window
    cv2.imshow("QR Code Scanner", frame)

    # Wait for the user to press a key
    key = cv2.waitKey(1)

    # If the user pressed the "q" key, break from the loop
    if key == ord("q"):
        break

# Release the camera
cap.release()

# Destroy all windows
cv2.destroyAllWindows()
