import cv2

img = cv2.imread(r"C:\Users\jayav\Downloads\gettyimages-88688360-594x594.jpg")

roi = img[100:300, 100:300]

img[0:200, 0:200] = roi

cv2.imshow("Modified Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()