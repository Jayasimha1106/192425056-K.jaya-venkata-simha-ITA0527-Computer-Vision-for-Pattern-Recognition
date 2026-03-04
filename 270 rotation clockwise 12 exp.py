import cv2

img = cv2.imread(r"C:\Users\jayav\OneDrive\Pictures\Screenshots\Screenshot 2026-02-27 145812.png")

# Rotate 270 degrees clockwise
rotated = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imshow('270 Degree Rotation', rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()