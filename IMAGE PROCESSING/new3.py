import cv2
import numpy as np
import path

def display_intensity_matrix(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    height, width = image.shape
    
    for i in range(height):
        for j in range(width):
            print(f'{image[i, j]:3}', end=' ')
        print()

input_image_path = path.img
display_intensity_matrix(input_image_path)