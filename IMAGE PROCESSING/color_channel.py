import cv2
import numpy as np

'''

Color Channel: A image consist of 3 color channel (BGR) BLUE GREEN RED which are merged together.

[ Image ].shape consist of 3 element height, width, color channel

'''
inp_img = cv2.imread("demo.jpg")
cv2.imshow("",inp_img)

# Splitting 3 channels
# blue,green,red = cv2.split(inp_img)
# cv2.imshow("BLUE CHANNEL", blue)
# cv2.imshow("GREEN CHANNEL", green)
# cv2.imshow("RED CHANNEL", red)

# Merging 3 channels
# org_img = cv2.merge([blue,green,red])
# cv2.imshow("MERGED",org_img)

# Reconstructing image
# blank_img = np.zeros(inp_img.shape[:2],dtype="uint8") # Creating an blank image
# blue_img = cv2.merge([blue, blank_img, blank_img])
# green_img = cv2.merge([blank_img, blue, blank_img])
# red_img = cv2.merge([blank_img, blank_img, red])
# cv2.imshow("BLUE CHANNEL", blue_img)
# cv2.imshow("GREEN CHANNEL", green_img)
# cv2.imshow("RED CHANNEL", red_img)
cv2.waitKey(0)