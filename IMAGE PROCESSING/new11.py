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
    # Apply the Prewitt operator for edge detection
    kernel_x = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
    kernel_y = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])
    
    prewitt_x = cv2.filter2D(image, -1, kernel_x)
    prewitt_y = cv2.filter2D(image, -1, kernel_y)

    # Calculate the magnitude of the gradient
    gradient_magnitude = np.sqrt(prewitt_x**2 + prewitt_y**2)

    # Normalize the gradient magnitude to the range [0, 255] using NumPy
    gradient_magnitude_normalized = ((gradient_magnitude - gradient_magnitude.min()) * 255 / (gradient_magnitude.max() - gradient_magnitude.min())).astype(np.uint8)

    # Display the original image and the edge-detected image
    cv2.imshow('Original Image', image)
    cv2.imshow('Edge-Detected Image (Prewitt Operator)', gradient_magnitude_normalized)
    
    # Save the Edge-Detected Image (Prewitt Operator)
    output_image_path = 'edge_detected_image.jpg'
    cv2.imwrite(output_image_path, gradient_magnitude_normalized)

    # Wait for a key press and then close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()