import cv2
import numpy as np
import path

def high_pass_filter(image, kernel_size=(3, 3)):
    # Convert the image to grayscale
    gray_image = image

    # Create a Gaussian blur filter
    blurred_image = cv2.GaussianBlur(gray_image, kernel_size, 0)

    # Calculate the high-pass filtered image
    high_pass_image = gray_image - blurred_image

    return high_pass_image

# Load the input image
image = cv2.imread(path.img, cv2.IMREAD_REDUCED_GRAYSCALE_2)

if image is None:
    print("Error: Could not load image.")
else:
    # Apply the high-pass filter
    high_pass_result = high_pass_filter(image)

    ## Display the original and high-pass filtered images
    #cv2.imshow('Original Image', image)
    #cv2.imshow('High-Pass Filtered Image', high_pass_result)

    # Save the high-pass filtered image
    cv2.imwrite('Highpass Filtered Image.jpg', high_pass_result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()