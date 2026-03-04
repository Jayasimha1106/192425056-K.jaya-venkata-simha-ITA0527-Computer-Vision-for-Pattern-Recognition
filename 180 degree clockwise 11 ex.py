import cv2

# Read image
img = cv2.imread(r"C:\Users\jayav\OneDrive\Pictures\Screenshots\Screenshot 2026-02-27 145812.png")

# Rotate 180 degrees
rotated = cv2.rotate(img, cv2.ROTATE_180)

cv2.imshow('180 Degree Rotation', rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()