"""
This code shows you how to apply the Sobel operator using the internal methods of the "scipy" module.

Pieces of code were used from the following link (it's worth taking a look!):
https://stackoverflow.com/questions/7185655/applying-the-sobel-filter-using-scipy

I changed some of their variable names to match how I've been using them in this tutorial
"""

import numpy as np
from matplotlib.image import imread
from scipy import ndimage
import matplotlib.pyplot as plt

fig = plt.figure()
ax1, ax2 = fig.add_subplot(121), fig.add_subplot(122)  # left and right image respectively

original_image = imread('Images/original_image.PNG')
dx, dy = ndimage.sobel(original_image, 0), ndimage.sobel(original_image, 1)  # apply Sobel in the x and y directions
sobel_filtered_image = np.hypot(dx, dy)  # is equal to ( dx ^ 2 + dy ^ 2 ) ^ 0.5
sobel_filtered_image = sobel_filtered_image / np.max(sobel_filtered_image)  # normalization step

ax1.imshow(original_image)
ax2.imshow(sobel_filtered_image)
plt.show()
