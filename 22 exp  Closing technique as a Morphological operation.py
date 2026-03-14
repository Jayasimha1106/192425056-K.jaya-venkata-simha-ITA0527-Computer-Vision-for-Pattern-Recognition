import cv2
import numpy as np

img = cv2.imread(r"C:\Users\jayav\Downloads\gettyimages-88688360-594x594.jpg", 0)

kernel = np.ones((5,5), np.uint8)

# Closing operation
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

cv2.imshow("Original Image", img)
cv2.imshow("Closing Result", closing)

cv2.waitKey(0)
cv2.destroyAllWindows()