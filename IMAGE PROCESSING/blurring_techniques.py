from cv2 import imread, imshow, waitKey, blur, GaussianBlur, medianBlur, bilateralFilter

'''

Bluring (Use to smoothing noise or edges)

Methods of bluring techniques: -
1) Average Blur: Center pixel of an kernel is sum of its surrounding pixel and their average.
2) Gaussian Blur: Center pixel of an kernel is average of each pixel with some defined weight and their products.
3) Median Blur: Center pixel of an kernel is sum of its surronding pixel and their median.
4) Bi-lateral Blur: Blurring an image without smoothing edges.

Note: -
    1. Kernel size can only be odd number starting from 3.
    2. Other name of kernel is convolution kernel / emboss
    3. sigma means amount of bluring.
'''

inp_img = imread('demo.jpg')
ksize = 5 # Kernel size
sigma = 0 # Amount of blurring


# Image Averaging
avg_img = blur(inp_img, (ksize,ksize))
imshow("Image Averaging", avg_img)

# Gaussian Blurring Image
gaussuan_img = GaussianBlur(inp_img, (ksize,ksize), sigma)
imshow("Gaussian Blurring Image", gaussuan_img)

# Median Blurring Image
median_img = medianBlur(inp_img, ksize)
imshow("Median Blurring Image", median_img)

# Bi-lateral Blurring Image
bilateral_img = bilateralFilter(inp_img, 5, 40, 40)
imshow("Bilateral Blurring Image",bilateral_img)

imshow("OUTPUT",inp_img)
waitKey(0)