import cv2
import numpy as np
import path

# Replace 'your_image.jpg' with the path to your image file
image_path = path.img

# Load the image
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Check if the image was loaded successfully
if image is None:
    print(f"Error: Unable to load image from {image_path}")
else:
    # Convert the image to float32 data type
    image_float = np.float32(image)

    # Apply logarithmic transformation to the image
    log_image = np.log1p(image_float)

    # Perform Fourier Transform
    fft_image = np.fft.fft2(log_image)

    # Create a Gaussian high-pass filter
    rows, cols = image.shape
    center_row, center_col = rows // 2, cols // 2
    x, y = np.meshgrid(np.arange(rows) - center_row, np.arange(cols) - center_col)
    sigma = 10

    highpass_filter = 1 - np.exp(-(x ** 2 + y ** 2) / (2 * (sigma ** 2)))
    
    # Apply the high-pass filter
    filtered_image = fft_image * highpass_filter		# problem length of fft_image and highpass_filter

    # Perform Inverse Fourier Transform
    filtered_image = np.fft.ifft2(filtered_image)

    # Exponentiate the result to undo the earlier logarithmic transformation
    filtered_image = np.expm1(np.real(filtered_image))

    # Normalize the output image to the range [0, 255]
    filtered_image = cv2.normalize(filtered_image, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

    # Display the original image and the homomorphically filtered image
    cv2.imshow('Original Image', image)
    cv2.imshow('Homomorphic Filtered Image', filtered_image)
    
    # Save the Homomorphically Filtered Image
    output_image_path = 'homomorphically_filtered_image.jpg'
    cv2.imwrite(output_image_path, filtered_image)

    # Wait for a key press and then close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()