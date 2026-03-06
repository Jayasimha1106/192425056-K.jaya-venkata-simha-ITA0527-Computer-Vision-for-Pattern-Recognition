import cv2
import numpy as np

img = cv2.imread(r"C:\Users\jayav\Downloads\gettyimages-88688360-594x594.jpg",0)

kernel = np.ones((5,5), np.uint8)

erosion = cv2.erode(img, kernel, iterations=1)

cv2.imshow("Original", img)
cv2.imshow("Eroded Image", erosion)

cv2.waitKey(0)
cv2.destroyAllWindows()