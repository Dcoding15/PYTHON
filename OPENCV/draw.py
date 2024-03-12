import cv2
import numpy as np

# Creating blank image
dimension = (900,900,3)  #(height, width, no. of color channel) in pixel
blank_img = np.zeros(dimension, dtype='uint8')

# Note: Atmost no. of color channel is 4 (Blue, Green, Red, Black)
#blank_img[:] = (0,0,225)    #(Blue, Green, Red)

# Paint certain part of an image
#        [ height, width  ]
#blank_img[100:300, 100:400] = (0,0,225)

# Draw a rectange or square
#Syntax: cv2.rectangle(image, point1, point2, color, thickness, linetype, shift)
#point1 = (100,100)  # (x1, y1)
#point2 = (250,200)  # (x2, y2)
#color = (0,225,0)   # (Blue, Green, Red)
#thickness = -1   # no. of pixel size. If -1 is provided then it will be fileed
#cv2.rectangle(blank_img, point1, point2, color, thickness)

# Draw a circle
#Syntax: cv2.circle(image, center, radius, color, thickness, lineype, shift)
#center = (100,100)
#radius = 50
#color = (0,225,0)
#thickness = -1
#cv2.circle(blank_img, center, radius, color, thickness)

# Draw a line
#Syntax: cv2.line(image, point1, point2, color, thickness, linetype, shift)
#pt1 = (100,100)
#pt2 = (500,100)
#color = (0,225,0)
#thickness = 5
#cv2.line(blank_img, pt1, pt2, color, thickness)

# Write a text
#Syntax: cv2.putText(image, text, point, font_face, size, color, thickness, linetype, bottomLeftOrigin)
'''
Font Face: -
FONT_HERSHEY_COMPLEX
FONT_HERSHEY_COMPLEX_SMALL
FONT_HERSHEY_DUPLEX
FONT_HERSHEY_PLAIN
FONT_HERSHEY_SCRIPT_COMPLEX
FONT_HERSHEY_SCRIPT_COMPLEX
FONT_HERSHEY_SIMPLEX
FONT_HERSHEY_TRIPLEX
'''
#text = 'Hello, World!'  # string text
#point = (100,100)   # (x, y)
#font_face = cv2.FONT_HERSHEY_SIMPLEX
#size = 2    # In centimeter
#color = (0,225,0)   # BGR
#thickness = 3   # pixel
#cv2.putText(blank_img, text, point, font_face, size, color, thickness)

cv2.imshow('Blank Image', blank_img)
cv2.waitKey(0)
