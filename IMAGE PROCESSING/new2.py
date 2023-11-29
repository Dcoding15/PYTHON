import cv2
from PIL import Image
import matplotlib.pyplot as plt
import path

def show_intensity_histogram(image_path):
    image = cv2.imread(image_path, cv2.COLOR_BGR2GRAY)
    
    # Calculate histogram
    histogram = cv2.calcHist([image], [0], None, [256], [0, 256])
    
    plt.figure(figsize=(10, 6))
    plt.plot(histogram)
    plt.title("Intensity Histogram")
    plt.xlabel("Intensity Value")
    plt.ylabel("Frequency")
    plt.xlim([0, 256])
    plt.show()

show_intensity_histogram(path.img)