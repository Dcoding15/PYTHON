import cv2
import numpy as np
import path
image_path = path.img
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
if image is None:
    print(f"Error: Unable to load image from {image_path}")
else:
    image_float = np.float32(image)
    log_image = np.log1p(image_float)
    fft_image = np.fft.fft2(log_image)
    rows, cols = image.shape
    center_row, center_col = rows // 2, cols // 2
    sigma = 2000
    x, y = np.indices(image.shape)
    highpass_filter = 1 - np.exp(-((x - center_row) ** 2 + (y - center_col) ** 2) / (2 * sigma ** 2))
    filtered_image = fft_image * highpass_filter
    filtered_image = np.fft.ifft2(filtered_image)
    filtered_image = np.expm1(np.real(filtered_image))
    filtered_image = cv2.normalize(filtered_image, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
    cv2.imwrite('Homomorphic Filtered Image.jpg', filtered_image)
