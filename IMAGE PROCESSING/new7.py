import cv2
import numpy as np
import path

def image_quantization():
    image = cv2.imread(path.img)
    num_colors = 16		# no. of colors for quantisation
    
    # Reshape the image to a 2D array of pixels
    pixels = image.reshape(image.shape)
    
    # Convert the pixel values to float32 for k-means
    pixels = np.float32(pixels)
    
    # Define criteria and apply k-means
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
    _, labels, centers = cv2.kmeans(pixels, num_colors, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    
    # Convert the centers back to uint8
    centers = np.uint8(centers)
    
    # Map each pixel to its corresponding center color
    quantized_image = centers[labels.flatten()]
    
    # Reshape the quantized image back to the original shape
    quantized_image = quantized_image.reshape(image.shape)
    
    cv2.imshow("Quantized Image", quantized_image)
    
	# Save the Quantized image
    cv2.imwrite('Quantized Image.jpg', quantized_image)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

image_quantization()