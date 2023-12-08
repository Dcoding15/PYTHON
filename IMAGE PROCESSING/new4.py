import cv2
import numpy as np
import path

def display_intensity_binary(image_path, threshold=128):
    image = cv2.imread(image_path, cv2.IMREAD_REDUCED_GRAYSCALE_8)
    height, width = image.shape
    
    for i in range(height):
        for j in range(width):
            binary_value = '1' if image[i, j] >= threshold else '0'
            print(binary_value, end='')
        print()

display_intensity_binary(path.img1)