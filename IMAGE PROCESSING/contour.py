'''

Contour Detection: -
    1. It is a process of finding and identifying boundries of an object within an image.
    2. Those boundries are represented as continuous curvers and lines.
    3. It is used for object-detection and image segmentation.
    4. Techniques like edge detection, gradient based methods, contour tracing, active contour models, the watershed algorithm, and convolutional neural networks (CNNs).

'''

import cv2
import numpy as np

inp_img = cv2.imread('demo.jpg')

# Convert BGR into GRAY image
gray_img = cv2.cvtColor(inp_img, cv2.COLOR_BGR2GRAY)

# Using Gaussian Blur to reduce no. of edges
#blur_img = cv2.GaussianBlur(gray_img, (3,3), cv2.BORDER_DEFAULT)

# Using Canny edge detection
edge_img = cv2.Canny(gray_img, 30, 30)

# Finding boundries in an image
contour, hierarchies = cv2.findContours(edge_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

print(f'No. of contours: {len(contour)}')


# Visualise contour from image
# cv2.drawContours(image, contour list, contour index, color, thickness=None, lineType=None, hierarchy=None, maxLevel=None, offset=None)
# Note: You can use -1 in contour index for taking all contour
blank_img = np.zeros(gray_img.shape, dtype='uint8')
start_index = 200
end_index = 500
for i in range(start_index,end_index):
    cv2.drawContours(blank_img, contour, i, (255,255,255), 1)

cv2.imshow('OUTPUT.jpg',edge_img)
cv2.imshow('VISUALISE CONTOUR.jpg', blank_img)
cv2.waitKey(0)
