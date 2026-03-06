import cv2

# Read images
img = cv2.imread(r"C:\Users\jayav\Downloads\gettyimages-88688360-594x594.jpg")
watermark = cv2.imread(r"C:\Users\jayav\Downloads\gettyimages-88688360-594x594.jpg")
# Resize watermark
watermark = cv2.resize(watermark, (150, 150))

# Get position
h, w, _ = watermark.shape
img[0:h, 0:w] = cv2.addWeighted(img[0:h, 0:w], 0.7, watermark, 0.3, 0)

# Show result
cv2.imshow("Watermarked Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()