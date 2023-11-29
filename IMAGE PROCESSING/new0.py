from PIL import Image
import path

# Open an image file
image_path = path.img  # Replace with the actual path to your image
image = Image.open(image_path)

# Display some basic information about the image
print("Image format:", image.format)
print("Image size:", image.size)
print("Image mode:", image.mode)  # This should be 'RGB' for color images

image = Image.open(image_path)

# Convert the image to grayscale
gray_image = image.convert('L')

# Display grayscale image information
print("Grayscale image format:", gray_image.format)
print("Grayscale image size:", gray_image.size)
print("Grayscale image mode:", gray_image.mode)

image = Image.open(image_path)

# Convert the image to grayscale if it's not already
gray_image = image.convert('L')

# Apply a binary threshold
threshold_value = 128  # Adjust this threshold value as needed
binary_image = gray_image.point(lambda p: p > threshold_value and 255)

# Display binary image information
print("Binary image format:", binary_image.format)
print("Binary image size:", binary_image.size)
print("Binary image mode:", binary_image.mode)

# Show the binary image
binary_image.show()

# Show the grayscale image
gray_image.show()

# Show the image (optional)
image.show()