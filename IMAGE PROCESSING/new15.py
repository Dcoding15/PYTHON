import cv2
import path

# Replace 'input_image.jpg' with the path to your input image
input_image_path = path.img

# Load the image
image = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)

# Check if the image is loaded successfully
if image is None:
    print("Error: Unable to load image.")
    exit()

# Perform Canny edge detection
edges = cv2.Canny(image, threshold1=100, threshold2=200)  # You can adjust the thresholds as needed

# Display the original image
cv2.imshow('Original Image', image)

# Display the Canny edge-detected image
cv2.imshow('Canny Edges', edges)

# Save the Edge-Detected Image (Canny Edge Detection)
output_image_path = 'canny_edge_detected_image.jpg'
cv2.imwrite(output_image_path, edges)

# Wait for a key press and then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()