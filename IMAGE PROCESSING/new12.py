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
    # Apply the Sobel operator for edge detection
    sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

    # Calculate the magnitude of the gradient
    gradient_magnitude = np.sqrt(sobel_x**2 + sobel_y**2)

    # Normalize the gradient magnitude to the range [0, 255]
    gradient_magnitude_normalized = cv2.normalize(gradient_magnitude, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

    # Display the original image and the edge-detected image
    cv2.imshow('Original Image', image)
    cv2.imshow('Edge-Detected Image', gradient_magnitude_normalized)
    
    # Save the Edge-Detected Image (Sobel Operator)
    output_image_path = 'edge_detected_image.jpg'
    cv2.imwrite(output_image_path, gradient_magnitude_normalized)

    # Wait for a key press and then close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()