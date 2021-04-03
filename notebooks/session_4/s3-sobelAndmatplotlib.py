import cv2
import numpy as np
import matplotlib.pyplot as plt
#Read the image as grayscale:
image = cv2.imread('building.jpg', 0)


#Compute the gradient approximations using the Sobel operator:
dx = cv2.Sobel(image, cv2.CV_32F, 1, 0)
dy = cv2.Sobel(image, cv2.CV_32F, 0, 1)

#Visualize the results:
plt.figure()
plt.subplot(141)
plt.axis('off')
plt.title('image')
plt.imshow(image, cmap='gray')

plt.subplot(142)
plt.axis('off')
plt.imshow(dx, cmap='gray')
plt.title('dx')

plt.subplot(143)
plt.axis('off')
plt.imshow(dy, cmap='gray')
plt.title('dx')

plt.subplot(144)
plt.axis('off')
plt.title('dy + dx')
plt.imshow(np.absolute(dx)+np.absolute(dy), cmap='gray')


plt.show()
