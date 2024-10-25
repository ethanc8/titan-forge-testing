import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)
    
while cap.isOpened():
    # Get frame
    ret, frame = cap.read()
    
    # Convert to HSV (Hue Value Saturation)
    raw_image = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # Color thresholds
    lower_threshold = np.array([20, 100, 100])
    upper_threshold = np.array([80, 255, 255])

    # Create mask
    mask = cv.inRange(raw_image, lower_threshold, upper_threshold)

    # Get contours
    contours, hierarchy = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    
    # Convert back to BGR, draw contours
    final_image = cv.cvtColor(raw_image, cv.COLOR_HSV2BGR)
    cv.drawContours(final_image, contours, -1, (0, 255, 0), 3)

    # new code here

    # Show frame
    cv.imshow("Mask", mask)
    cv.imshow("Feed", final_image)

    # Quit if Q is pressed
    if cv.waitKey(1) == ord('q'):
        break


# Close window
cap.release()
cv.destroyAllWindows()
