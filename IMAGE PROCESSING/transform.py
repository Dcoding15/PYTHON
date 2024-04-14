import cv2
import numpy as np

# Image translation - shifting an image along with x-axis and y-axis
def translating(image, x_axis, y_axis):
    '''
        x axis --> -ve value shift image to left & +ve value shift image to right.
        y axis --> -ve value shift image to up & +ve value shift image to down.
    '''
    translate_matrix = np.float32([[1,0,x_axis],[0,1,y_axis]])
    dimension = (image.shape[1], image.shape[0])    #(height, width)
    return cv2.warpAffine(image, translate_matrix, dimension)

# Image rotation
def rotating(image, angle, center=None, scale=None):
    '''
        Angle --> -ve value rotate image clockwise & +ve rotate image anti-clockwise.
    '''
    height, width = image.shape[1], image.shape[0]
    center = (width//2,height//2) if center is None else center
    scale = 1 if scale is None else scale
    rotate_matrix = cv2.getRotationMatrix2D(center, angle, scale)
    return cv2.warpAffine(image, rotate_matrix, (width, height))

# Image flip
def flipping(image, flip_code):
    '''
        flip_code: -
        0 --> flip image vertically
        1 --> flip image horizontally
        -1 --> image first flip horizontally and then image flip vertically
    '''
    return cv2.flip(image, flip_code)

inp_img = cv2.imread('demo.jpg')
cv2.imshow('Demo Image', flipping(inp_img, -1))
cv2.waitKey(0)
