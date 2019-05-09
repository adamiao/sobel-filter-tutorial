"""
There is a lot of good information out there related to this topic. The image used in this example was extracted from:
https://en.wikipedia.org/wiki/Sobel_operator

The same concepts explained in this code can be used for other types of filters.

For grayscale transformation of images there are a ton of references on the web. A straightforward one would be to go
to our old friend Wikipedia:
https://en.wikipedia.org/wiki/Grayscale
"""

from matplotlib.image import imread
import matplotlib.pyplot as plt
import numpy as np

# #------------------------------------------------------------------------------
# PART I - Transforming a color image into grayscale
# #------------------------------------------------------------------------------

# Here we import the image file as a tensor of shape (nx, ny, nz)
photo_file = 'Images/original_image.PNG'
input_image = imread(photo_file)
[nx, ny, nz] = np.shape(input_image)  # nx: height, ny: width, nz: colors (RGB)

# Extracting each one of the RGB components
# r_img, g_img, b_img = input_image[:, :, 0], input_image[:, :, 1], input_image[:, :, 2]
r_img, g_img, b_img = input_image[:, :, 0] / 255, input_image[:, :, 1] / 255, input_image[:, :, 2] / 255

# To make it grayscale we can use the following constants to weight
# r_const, g_const, b_const = 0.2989, 0.5870, 0.1140
r_const, g_const, b_const = 0.2126, 0.7152, 0.0722

# A weighted average of each color component will give us the grayscale image
# grayscale = r_const*r_img + g_const*g_img + b_const*b_img
gamma = 1.0
grayscale = (r_const*r_img**gamma + g_const*g_img**gamma + b_const*b_img**gamma)*255

# This command will display the image on the screen
# plt.imshow(grayscale, cmap=plt.get_cmap('gray'))
# plt.show()

# #------------------------------------------------------------------------------
# PART II - Applying the kernel Gx and Gy to image
# #------------------------------------------------------------------------------

"""
The kernels Gx and Gy can be thought of as a differential operation in the input_image of the input image 
in the directions x and y respectively. These kernels are given by:
      _               _                   _                _
     |                 |                 |                  |
     | 1.0   0.0  -1.0 |                 |  1.0   2.0   1.0 |
Gx = | 2.0   0.0  -2.0 |    and     Gy = |  0.0   0.0   0.0 |
     | 1.0   0.0  -1.0 |                 | -1.0  -2.0  -1.0 |
     |_               _|                 |_                _|
"""

# This chunk of code defines the kernel operations and outputs image
Gx = np.array([[1.0, 0.0, -1.0], [2.0, 0.0, -2.0], [1.0, 0.0, -1.0]])
Gy = np.array([[1.0, 2.0, 1.0], [0.0, 0.0, 0.0], [-1.0, -2.0, -1.0]])
[rows, columns] = np.shape(grayscale)
sobel_filtered_image = np.zeros(shape=(rows, columns))
for i in range(rows - 2):
    for j in range(columns - 2):
        s1 = np.sum(np.multiply(Gx, grayscale[i:i+3, j:j+3]))
        s2 = np.sum(np.multiply(Gy, grayscale[i:i+3, j:j+3]))
        sobel_filtered_image[i + 1, j + 1] = np.sqrt(s1 ** 2 + s2 ** 2)


# Change the data type for the images we want to display
sobel_filtered_image = sobel_filtered_image.astype('int32')
input_image = input_image.astype('int32')

# Display the images

fig = plt.figure()
# plt.gray()  # show the filtered result in grayscale
ax1 = fig.add_subplot(121)  # left side
ax2 = fig.add_subplot(122)  # right side

ax1.imshow(input_image)
ax2.imshow(sobel_filtered_image, cmap=plt.get_cmap('gray'))
plt.show()

# Save the filtered image in destination path
plt.imsave('test_sobel_filtered_image.png', sobel_filtered_image, cmap=plt.get_cmap('gray'))
