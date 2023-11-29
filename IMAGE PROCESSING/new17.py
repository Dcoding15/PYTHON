import cv2
import numpy as np
import path

# Load an image from file
image_path = path.img# Replace 'your_image.jpg' with the path to your image
image = cv2.imread(image_path)

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Threshold the image to create markers for seeds
_, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Perform morphological operations to remove small noise
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

# Finding sure background and sure foreground areas
sure_bg = cv2.dilate(opening, kernel, iterations=3)
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
_, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)

# Finding unknown region
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)

# Label markers for watershed
_, markers = cv2.connectedComponents(sure_fg)
markers = markers + 1
markers[unknown == 255] = 0

# Apply the watershed algorithm
cv2.watershed(image, markers)
image[markers == -1] = [0, 0, 255]  # Mark watershed boundaries in red

# Display the result
cv2.imshow('Watershed Segmentation', image)

# Save the Watershed Segmentation
output_image_path = 'watershed_segmentation_image.jpg'
cv2.imwrite(output_image_path, image)

cv2.waitKey(0)
cv2.destroyAllWindows()