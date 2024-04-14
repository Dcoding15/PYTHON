import cv2

# Syntax: cv2.imread([path of an image])
img = cv2.imread("demo.jpg")

# Syntax: cv2.imshow([image name], [image])
cv2.imshow("DEMO PIC", img)

cv2.waitKey(0)  # Wait for infinite amount of time and exits if alt key press


