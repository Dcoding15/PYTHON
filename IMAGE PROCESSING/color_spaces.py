import cv2

'''

Color Space: These are different types of color modes. There are many color space that is popular and also has extensive use such as RGB, CMYK, etc.

Note: -
    1. For image processing always use BGR color model. RGB is used only for display image.
    2. From BGR color space we can convert to anything.
'''

inp_img = cv2.imread("demo.jpg")

# Convert BGR (Blue Green Red) to Grayscale
gray_img = cv2.cvtColor(inp_img, cv2.COLOR_BGR2GRAY)

# Convert BGR (Blue Red Green) to HSV (Hue Saturation Value)
hsv_img = cv2.cvtColor(inp_img, cv2.COLOR_BGR2HSV)

# Convert BGR to L A B (L* represents lightness from black to white on a scale of zero to 100, while a* and b* represent chromaticity with no specific numeric limits)
lab_img = cv2.cvtColor(inp_img, cv2.COLOR_BGR2LAB)

# Convert BGR (Blue Green Red) to RGB (Reb Blue Green)
rgb_img = cv2.cvtColor(inp_img,cv2.COLOR_BGR2RGB)

cv2.imshow("ORIGINAL",inp_img)
cv2.imshow("OUTPUT",rgb_img)
cv2.waitKey(0)