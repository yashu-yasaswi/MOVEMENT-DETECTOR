import cv2

# Open the default camera
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    
    # If the frame is captured successfully
    if ret:
        blurred = cv2.GaussianBlur(gray,(21,21),0)
        ret,thresh = cv2.threshold(gray,20,255,cv2.THRESH_BINARY)
        dilated=cv2.dilate(gray,None,iterations=2)


        cv2.imshow("blurred", blurred)
        cv2.imshow("dilated",dilated)
        cv2.imshow("thresh",thresh)
    else:
        break
    
    # Check for the 'q' key to exit the loop
    k = cv2.waitKey(10)  # Corrected to cv2.waitKey with a capital 'K'
    if k == ord('q'):
        break

# Release the capture and close all OpenCV windows
#cap.release()
cv2.destroyAllWindows()  # Corrected to destroyAllWindows with a capital 'W'
