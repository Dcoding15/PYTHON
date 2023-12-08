import cv2
import numpy as np
import path

def display_intensity_matrix(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_REDUCED_GRAYSCALE_8)
    height, width = image.shape
    
    for i in range(height):
        for j in range(width):
            print(f'{image[i, j]:3}', end=' ')
        print()

display_intensity_matrix(path.img1)
