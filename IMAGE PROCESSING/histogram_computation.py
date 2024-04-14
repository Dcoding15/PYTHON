'''

Histogram visualise the distribution of pixel intensity by plotting graph 

'''
#pylint:disable=no-member

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('demo.jpg')
blank = np.zeros(img.shape[:2], dtype='uint8')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
mask = cv.circle(blank, (img.shape[1]//2,img.shape[0]//2), 150, 255, -1)
masked = cv.bitwise_and(img,img,mask=mask)
cv.imshow("MASKED",masked)

# GRayscale histogram
gray_hist = cv.calcHist([masked], [0], mask, [256], [0,256] )

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

# Colour Histogram

plt.figure()
plt.title('Colour Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors = ('b', 'g', 'r')
for i,col in enumerate(colors):
    hist = cv.calcHist([masked], [i], mask, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])
plt.show()

cv.waitKey(0)