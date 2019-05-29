"""
This code shows you how to apply the Sobel operator using the methods of the "scipy" module.

Pieces of code were used from the following link (it's worth taking a look!):
https://stackoverflow.com/questions/7185655/applying-the-sobel-filter-using-scipy

I changed some of their variable names to match how I've been using them in this tutorial.

The image used in this example was extracted from: https://en.wikipedia.org/wiki/Sobel_operator
"""

import numpy as np
from matplotlib.image import imread
from scipy import ndimage
import matplotlib.pyplot as plt

# Here we read the image and bring it as an array
original_image = imread('Images/original_image.PNG')

# Next we apply the Sobel filter in the x and y directions to then calculate the output image
dx, dy = ndimage.sobel(original_image, axis=0), ndimage.sobel(original_image, axis=1)
sobel_filtered_image = np.hypot(dx, dy)  # is equal to ( dx ^ 2 + dy ^ 2 ) ^ 0.5
sobel_filtered_image = sobel_filtered_image / np.max(sobel_filtered_image)  # normalization step

# Display and compare input and output images
fig = plt.figure(1)
ax1, ax2 = fig.add_subplot(121), fig.add_subplot(122)
ax1.imshow(original_image)
ax2.imshow(sobel_filtered_image, cmap=plt.get_cmap('gray'))
plt.show()
