import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# Read the first two frames
ret1, frame1 = cap.read()
ret2, frame2 = cap.read()

while True:
    # Convert frames to grayscale
    frame1_gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    frame2_gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to the grayscale frames
    frame1_blur = cv2.GaussianBlur(frame1_gray, (21, 21), 0)
    frame2_blur = cv2.GaussianBlur(frame2_gray, (21, 21), 0)

    # Compute the absolute difference between the blurred frames
    diff = cv2.absdiff(frame1_blur, frame2_blur)

    # Display the difference
    thresh = cv2.threshold(diff,20,255, cv2.THRESH_BINARY)[1]
    final = cv2.dilate(thresh, None, iterations=2)

    masked = cv2.bitwise_and (frame1, frame1, mask=thresh)

    white_pixels = np.sum(thresh)/255
    rows,cols=thresh.shape
    total = rows* cols
    if white_pixels>0.01*total:
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame1,'Movement Detected', (10,50),font,1,(0,0,255), 2, cv2.LINE_AA)

    cv2.imshow("Motion", frame1)

    # Move to the next frame
    frame1 = frame2
    ret, frame2 = cap.read()

    # If the frame cannot be captured, exit the loop
    if not ret:
        break

    # Break the loop if the 'q' key is pressed
    k = cv2.waitKey(10)  # Corrected to cv2.waitKey with a capital 'K'
    if k == ord('q'):
        break

# Release the capture and close all OpenCV windows
#cap.release()
cv2.destroyAllWindows()  # Corrected to destroyAllWindows with a capital 'W'
