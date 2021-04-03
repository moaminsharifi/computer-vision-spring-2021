import cv2
import numpy as np
import matplotlib.pyplot as plt

#Load an image, convert it to floating-point, and scale it down to the [0, 1] range:
image = cv2.imread('5.jpg').astype(np.float32) / 255

#Create noise in the image by adding random values to each pixel, and display it: 
noised = (image + 0.2 * np.random.rand(*image.shape).astype(np.float32))
noised = noised.clip(0, 1)
cv2.imshow('',noised)
plt.imshow(noised[:,:,[2,1,0]])
plt.show()

#Apply GaussianBlur to the noisy image and show the result:
gauss_blur = cv2.GaussianBlur(noised, (7, 7), 0)
plt.imshow(gauss_blur[:, :, [2, 1, 0]])
plt.show()

#Apply median filtering:
median_blur = cv2.medianBlur((noised * 255).astype(np.uint8), 7)
plt.imshow(median_blur[:, :, [2, 1, 0]])
plt.show()

#Perform median filtration to our image with noise:
bilat = cv2.bilateralFilter(noised, -1, 0.3, 10)
plt.imshow(bilat[:, :, [2, 1, 0]])
plt.show()
