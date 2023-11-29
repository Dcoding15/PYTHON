import numpy as np
import cv2
import matplotlib.pyplot as plt
import path

# Load the image in grayscale
image_path = path.img
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Apply Sobel edge detection
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
sobel_edges = np.sqrt(sobel_x**2 + sobel_y**2)

# Apply Scharr edge detection
scharr_x = cv2.Scharr(image, cv2.CV_64F, 1, 0)
scharr_y = cv2.Scharr(image, cv2.CV_64F, 0, 1)
scharr_edges = np.sqrt(scharr_x**2 + scharr_y**2)

# Apply Canny edge detection
canny_edges = cv2.Canny(image, threshold1=100, threshold2=200)

# Display the original image and edge detection results
plt.figure(figsize=(15, 10))

plt.subplot(2, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(sobel_edges, cmap='gray')
plt.title('Sobel Edges')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(scharr_edges, cmap='gray')
plt.title('Scharr Edges')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(canny_edges, cmap='gray')
plt.title('Canny Edges')
plt.axis('off')

plt.tight_layout()
plt.show()