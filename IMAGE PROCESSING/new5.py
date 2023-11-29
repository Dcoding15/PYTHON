from PIL import Image
import matplotlib.pyplot as plt
import path

def display_channels(image_path):
    # Open the image using PIL
    image = Image.open(image_path)
    
    # Split the image into its RGB channels
    red_channel, green_channel, blue_channel = image, image, image

    # Display the red, green, and blue channels using matplotlib
    plt.figure(figsize=(10, 4))
    
    plt.subplot(1, 3, 1)
    plt.imshow(red_channel, cmap='Reds')
    plt.title('Red Channel')
    
    plt.subplot(1, 3, 2)
    plt.imshow(green_channel, cmap='Greens')
    plt.title('Green Channel')
    
    plt.subplot(1, 3, 3)
    plt.imshow(blue_channel, cmap='Blues')
    plt.title('Blue Channel')
    
    plt.tight_layout()
    plt.show()

# Path to the input image
input_image_path = path.img

# Display the red, green, and blue channels of the image
display_channels(input_image_path)