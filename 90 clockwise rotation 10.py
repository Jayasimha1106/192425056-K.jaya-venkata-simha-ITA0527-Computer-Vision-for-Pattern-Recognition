import cv2

img = cv2.imread(r"C:\Users\jayav\OneDrive\Pictures\Screenshots\Screenshot 2026-02-27 145812.png")

rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

cv2.imshow("Original Image", img)
cv2.imshow("Rotated Image (90° Clockwise)", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()