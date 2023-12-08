import cv2
import numpy as np
import path

def band_pass_filter(image, low_cutoff, high_cutoff, kernel_size=(15, 15)):
    # Convert the image to grayscale
    gray_image = image

    # Apply a low-pass filter (Gaussian blur) to the image
    low_pass_filtered = cv2.GaussianBlur(gray_image, kernel_size, 0)

    # Apply a high-pass filter to the image
    high_pass_filtered = gray_image - low_pass_filtered

    # Create a binary mask for the band-pass filter
    mask = np.logical_and(high_pass_filtered >= low_cutoff, high_pass_filtered <= high_cutoff)

    # Apply the mask to the high-pass filtered image
    band_pass_result = np.where(mask, high_pass_filtered, 0)

    return band_pass_result

# Load the input image
image = cv2.imread(path.img, cv2.IMREAD_REDUCED_GRAYSCALE_2)

if image is None:
    print("Error: Could not load image.")
else:
    # Define the cutoff frequencies for the band-pass filter
    low_cutoff = 10
    high_cutoff = 200

    # Apply the band-pass filter
    band_pass_result = band_pass_filter(image, low_cutoff, high_cutoff)

    # Display the original and band-pass filtered images
    #cv2.imshow('Original Image', image)
    #cv2.imshow('Band-Pass Filtered Image', band_pass_result)

    # Save the band-pass filtered image
    cv2.imwrite('Bandpass Filtered Image.jpg', band_pass_result)

    # Add a delay and wait for a key press to close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()