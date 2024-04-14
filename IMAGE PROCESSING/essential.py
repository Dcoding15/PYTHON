import cv2
import numpy as np

input_img = cv2.imread('demo.jpg')
input_img = cv2.resize(input_img, (900,900), interpolation=cv2.INTER_AREA)

# Image gray scaling
gray_img = cv2.cvtColor(input_img, cv2.COLOR_BGR2GRAY)

# Image blurring
#Syntax: cv2.GaussianBlur(input_image, kernel_size, sigmaX, output_image, sigmaY,  borderType)
'''
Note: -
1. kernel_size should always be in odd positive number. (width, height)
2. sigmaX is Gaussian kernel standard deviation in X direction
3. sigmaY is Gaussian kernel standard deviation in Y direction
4. If sigmaY is zero then it is equal to sigmaX. If both sigma are zero then sigmaX = kernel_size.width and sigmaY = kernel_size.height
'''
blur_img = cv2.GaussianBlur(input_img, (5,5), cv2.BORDER_DEFAULT)

# Image Sharpening
#Syntax: cv2.Canny(image, thrshld1, thrshld2, edges, aperture_size, l2gradient)
sharp_img = cv2.Canny(blur_img, 175, 175)

'''
Note: -
    1. We can reduce the amount of edges by blurring the image.
    2. Image threasholding is the process of converting an image into grey scale to binary image according to pixel intensity. 
'''

# Image dilating
#Syntax: cv2.dilate(image, kernel_size, output_image, anchor, iterations, borderType, borderValue)
dilate_img = cv2.dilate(sharp_img, (5,5), iterations=3)

# Image eroding
#Syntax: cv2.erode(image, kernel_size, output_image, anchor, iterations, borderType, borderValue)
erode_img = cv2.erode(dilate_img, (5,5), iterations=3)

'''
Note: -
    1. No. of iterations = thickness of edges
    2. Image eroding is opposite of image dilation
'''

# Cropping Image using array slicing
#Syntax: image_variable[x1:y1, x2,y2]
cv2.imshow('Cropped Image', dilate_img[210:293, 200:400])

cv2.imshow("Essential Image", dilate_img)
cv2.waitKey(0)
