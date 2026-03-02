import cv2
import numpy as np

# Read image
img = cv2.imread("C:/Users/jayav/OneDrive/Pictures/Screenshots/Screenshot 2026-02-27 145812.png")

# Create kernel
kernel = np.ones((5,5), np.uint8)

# Apply erosion
eroded = cv2.erode(img, kernel, iterations=1)

# Show images
cv2.imshow("Original Image", img)
cv2.imshow("Eroded Image", eroded)

cv2.waitKey(0)
cv2.destroyAllWindows()