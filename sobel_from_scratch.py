"""
There is a lot of good information out there related to this topic. The image used in this example was extracted from:
https://en.wikipedia.org/wiki/Sobel_operator

The same concepts explained in this code can be used for other types of filters.

A color image is an array of dimension N x M x 3 where N is the height (number of rows), M is the width (number of
columns) and 3 is related to the colors red, green, blue composing the image.

A grayscale_image image is an array of dimension N x M.

There are lots of good information about color to grayscale_image image transformations out there on the web. The following
link has a very interesting discussion of how to properly do it:
https://stackoverflow.com/questions/687261/converting-rgb-to-grayscale-intensity
You can also find some good information at https://en.wikipedia.org/wiki/Grayscale.
"""

from matplotlib.image import imread
import matplotlib.pyplot as plt
import numpy as np

# #------------------------------------------------------------------------------
# PART I - Transforming an image from color to grayscale_image
# #------------------------------------------------------------------------------

# Here we import the image file as a tensor of shape (nx, ny, nz)
image_file = 'Images/original_image.PNG'
input_image = imread(image_file)  # this is the array representation of the input image
[nx, ny, nz] = np.shape(input_image)  # nx: height, ny: width, nz: colors (RGB)

# Extracting each one of the RGB components
r_img, g_img, b_img = input_image[:, :, 0], input_image[:, :, 1], input_image[:, :, 2]

# To make it grayscale_image we can use the following constants to weight
# r_const, g_const, b_const = 0.2989, 0.5870, 0.1140
# grayscale_image = r_const*r_img + g_const*g_img + b_const*b_img

# A weighted average of each color component will give us the grayscale_image image
gamma = 1.343
r_const, g_const, b_const = 0.2126, 0.7152, 0.0722
grayscale_image = (r_const * r_img ** gamma + g_const * g_img ** gamma + b_const * b_img ** gamma)

# This command will display the grayscale_image image
# plt.imshow(grayscale_image, cmap=plt.get_cmap('gray'))
# plt.show()

# #------------------------------------------------------------------------------
# PART II - Applying the kernel Gx and Gy to an image
# #------------------------------------------------------------------------------

"""
The kernels Gx and Gy can be thought of as a differential operation in the "input_image" array in the directions x and y 
respectively. These kernels are given by:
      _               _                   _                _
     |                 |                 |                  |
     | 1.0   0.0  -1.0 |                 |  1.0   2.0   1.0 |
Gx = | 2.0   0.0  -2.0 |    and     Gy = |  0.0   0.0   0.0 |
     | 1.0   0.0  -1.0 |                 | -1.0  -2.0  -1.0 |
     |_               _|                 |_                _|
"""

# Here we define the matrices associated with the Sobel filter
Gx = np.array([[1.0, 0.0, -1.0], [2.0, 0.0, -2.0], [1.0, 0.0, -1.0]])
Gy = np.array([[1.0, 2.0, 1.0], [0.0, 0.0, 0.0], [-1.0, -2.0, -1.0]])
[rows, columns] = np.shape(grayscale_image)
sobel_filtered_image = np.zeros(shape=(rows, columns))
for i in range(rows - 2):
    for j in range(columns - 2):
        s1 = np.sum(np.multiply(Gx, grayscale_image[i:i + 3, j:j + 3]))
        s2 = np.sum(np.multiply(Gy, grayscale_image[i:i + 3, j:j + 3]))
        sobel_filtered_image[i + 1, j + 1] = np.sqrt(s1 ** 2 + s2 ** 2)


# Display the images
fig = plt.figure()
ax1, ax2 = fig.add_subplot(121), fig.add_subplot(122)  # left and right image respectively

ax1.imshow(input_image, cmap=plt.get_cmap('gray'))
ax2.imshow(sobel_filtered_image, cmap=plt.get_cmap('gray'))
plt.show()

# Save the filtered image in destination path
# plt.imsave('test_sobel_filtered_image.png', sobel_filtered_image, cmap=plt.get_cmap('gray'))
