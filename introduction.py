"""
Small script describing how to display an image based on some input array as well as explaining how to apply the Sobel
operator/filter to a small patch of image.
"""

import numpy as np
import matplotlib.pyplot as plt

# Example of a grayscale image patch
A = np.array([[119, 80, 122], [177, 154, 212], [89, 25, 152]])
plt.imshow(A, cmap=plt.get_cmap('gray'))

# This chunk of code defines the kernel operations for the Sobel filter
Gx = np.array([[1.0, 0.0, -1.0], [2.0, 0.0, -2.0], [1.0, 0.0, -1.0]])
Gy = np.array([[1.0, 2.0, 1.0], [0.0, 0.0, 0.0], [-1.0, -2.0, -1.0]])

# The output of the kernel operation is given by the following
GxA, GyA = np.sum(np.multiply(Gx, A)), np.sum(np.multiply(Gy, A))
output_value = np.sqrt(GxA**2 + GyA**2)  # equal to the "hypotenuse" of the values in the x and y directions
print("output pixel value =", output_value)
