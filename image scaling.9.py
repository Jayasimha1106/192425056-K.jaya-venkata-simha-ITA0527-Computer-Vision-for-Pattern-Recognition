import cv2

img = cv2.imread(r"C:\Users\jayav\OneDrive\Pictures\Screenshots\Screenshot 2026-02-27 145812.png")

# Resize smaller (50%)
small = cv2.resize(img, None, fx=0.5, fy=0.5)

# Resize bigger (150%)
big = cv2.resize(img, None, fx=1.5, fy=1.5)

cv2.imshow("Original", img)
cv2.imshow("Smaller Image", small)
cv2.imshow("Bigger Image", big)

cv2.waitKey(0)
cv2.destroyAllWindows()