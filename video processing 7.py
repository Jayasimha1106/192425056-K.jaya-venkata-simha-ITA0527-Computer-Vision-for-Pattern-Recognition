import cv2

# Open saved video
cap = cv2.VideoCapture(r"C:\Users\jayav\Downloads\20752414-uhd_2160_3840_60fps.mp4")

if not cap.isOpened():
    print("Cannot open video")
    exit()

delay = 30  # Normal speed

print("Press 1 = Normal | 2 = Slow | 3 = Fast | q = Quit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Resize to fixed width (800 pixels)
    width = 800
    height = int(frame.shape[0] * (width / frame.shape[1]))
    resized = cv2.resize(frame, (width, height))

    cv2.imshow("Video Player", resized)

    key = cv2.waitKey(delay) & 0xFF

    if key == ord('n'):
        delay = 30      # Normal
    elif key == ord('s'):
        delay = 100     # Slow
    elif key == ord('f'):
        delay = 5       # Fast
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()