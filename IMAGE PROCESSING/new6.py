import cv2
import numpy as np
import path

def image_sampling(image_path, scale_factor):
    image = cv2.imread(image_path)
    if image is None:
        print("Error loading image.")
        return

    height, width, channels = image.shape
    new_height = int(height * scale_factor)
    new_width = int(width * scale_factor)

    sampled_image = np.zeros((new_height, new_width, channels), dtype=np.uint8)

    for i in range(new_height):
        for j in range(new_width):
            sampled_image[i, j] = image[int(i / scale_factor), int(j / scale_factor)]

    return sampled_image

input_image_path = path.img

scale_factors = [0.1, 0.3, 0.5, 0.7]

for idx, scale_factor in enumerate(scale_factors):
    sampled_image = image_sampling(input_image_path, scale_factor)
    window_name = f"Sampled Image {idx + 1}"
    cv2.imshow(window_name, sampled_image)
    # Save the Sampling image
    output_image_path = f'image_sampling{idx + 1}.jpg'
    cv2.imwrite(output_image_path, sampled_image)

cv2.waitKey(0)
cv2.destroyAllWindows()