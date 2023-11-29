import cv2
import path

def median_filter(image, kernel_size=3):
    # Apply the median filter to the image
    filtered_image = cv2.medianBlur(image, kernel_size)
    return filtered_image

# Load the input image
input_image_path = path.img
image = cv2.imread(input_image_path)

if image is None:
    print("Error: Could not load image.")
else:
    # Define the kernel size for the median filter
    kernel_size = 5

    # Apply the median filter
    median_filtered_image = median_filter(image, kernel_size)

    # Display the original and median filtered images
    cv2.imshow('Original Image', image)
    cv2.imshow('Median Filtered Image', median_filtered_image)

    # Save the median filtered image
    output_image_path = 'median_filtered_image.jpg'
    cv2.imwrite(output_image_path, median_filtered_image)

    # Add a delay and wait for a key press to close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()