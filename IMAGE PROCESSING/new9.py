import cv2
import numpy as np
import path

def high_pass_filter(image, kernel_size=(3, 3)):
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Create a Gaussian blur filter
    blurred_image = cv2.GaussianBlur(gray_image, kernel_size, 0)

    # Calculate the high-pass filtered image
    high_pass_image = gray_image - blurred_image

    return high_pass_image

# Load the input image
input_image_path = path.img
image = cv2.imread(input_image_path)

if image is None:
    print("Error: Could not load image.")
else:
    # Apply the high-pass filter
    high_pass_result = high_pass_filter(image)

    # Display the original and high-pass filtered images
    cv2.imshow('Original Image', image)
    cv2.imshow('High-Pass Filtered Image', high_pass_result)

    # Save the high-pass filtered image
    output_image_path = 'high_pass_filtered_image.jpg'
    cv2.imwrite(output_image_path, high_pass_result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()