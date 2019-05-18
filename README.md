In this tutorial we will construct and apply Sobel filters with the intent of extracting an image's edges. The kernels that will be used for this purpose are the following:


<img src="https://latex.codecogs.com/gif.latex?G_x=\begin{bmatrix}&space;1&space;&&space;0&space;&&space;-1&space;\\&space;2&space;&&space;0&space;&&space;-2&space;\\&space;1&space;&&space;0&space;&&space;-1&space;\end{bmatrix}\quad\text{and}\quad&space;G_y=\begin{bmatrix}&space;1&space;&&space;2&space;&&space;1&space;\\&space;0&space;&&space;0&space;&&space;0&space;\\&space;-1&space;&&space;-2&space;&&space;-1&space;\end{bmatrix}" title="G_x=\begin{bmatrix} 1 & 0 & -1 \\ 2 & 0 & -2 \\ 1 & 0 & -1 \end{bmatrix}\quad\text{and}\quad G_y=\begin{bmatrix} 1 & 2 & 1 \\ 0 & 0 & 0 \\ -1 & -2 & -1 \end{bmatrix}" />

Say we are given a 3 by 3 patch of image, denoted by <img src="https://latex.codecogs.com/gif.latex?$$A$$" />, from the original image. Then the output pixel from the operation will be given by:

<img src="https://latex.codecogs.com/gif.latex?\sqrt{\Big[G_x(A)\Big]^2+\Big[G_y(A)\Big]^2" />


Still under construction...
