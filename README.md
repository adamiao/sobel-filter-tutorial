In this tutorial we will construct and apply Sobel filters with the intent of extracting an image's edges. The kernels that will be used for this purpose are the following:


<img src="https://latex.codecogs.com/gif.latex?G_x=\begin{bmatrix}&space;1&space;&&space;0&space;&&space;-1&space;\\&space;2&space;&&space;0&space;&&space;-2&space;\\&space;1&space;&&space;0&space;&&space;-1&space;\end{bmatrix}\quad\text{and}\quad&space;G_y=\begin{bmatrix}&space;1&space;&&space;2&space;&&space;1&space;\\&space;0&space;&&space;0&space;&&space;0&space;\\&space;-1&space;&&space;-2&space;&&space;-1&space;\end{bmatrix}" title="G_x=\begin{bmatrix} 1 & 0 & -1 \\ 2 & 0 & -2 \\ 1 & 0 & -1 \end{bmatrix}\quad\text{and}\quad G_y=\begin{bmatrix} 1 & 2 & 1 \\ 0 & 0 & 0 \\ -1 & -2 & -1 \end{bmatrix}" />

Say we are given a 3 by 3 patch of image, denoted by <img src="https://latex.codecogs.com/gif.latex?$$A$$" />, from the original image. Then the output pixel from the operation will be given by:

<img src="https://latex.codecogs.com/gif.latex?\sqrt{\big[G_x(A)\big]^2+\big[G_y(A)\big]^2" />

For example, if you have the following patch of grayscale image:

<img src="https://latex.codecogs.com/gif.latex?A=\begin{bmatrix}&space;119&space;&&space;80&space;&&space;122&space;\\&space;177&space;&&space;154&space;&&space;212&space;\\&space;89&space;&&space;25&space;&&space;152&space;\end{bmatrix}" />

Then the output from the operations is:

<img src="https://latex.codecogs.com/gif.latex?G_x\big(A\big)=\begin{bmatrix}&space;1&space;&&space;0&space;&&space;-1&space;\\&space;2&space;&&space;0&space;&&space;-2&space;\\&space;1&space;&&space;0&space;&&space;-1&space;\end{bmatrix}\quad\text{and}\quad&space;G_y\big(A\big)=\begin{bmatrix}&space;1&space;&&space;2&space;&&space;1&space;\\&space;0&space;&&space;0&space;&&space;0&space;\\&space;-1&space;&&space;-2&space;&&space;-1&space;\end{bmatrix}" title="G_x=\begin{bmatrix} 1 & 0 & -1 \\ 2 & 0 & -2 \\ 1 & 0 & -1 \end{bmatrix}\quad\text{and}\quad G_y=\begin{bmatrix} 1 & 2 & 1 \\ 0 & 0 & 0 \\ -1 & -2 & -1 \end{bmatrix}" />

<img src="https://latex.codecogs.com/gif.latex?\sqrt{\big[G_x(A)\big]^2+\big[G_y(A)\big]^2=467" />

For now it's ok to have values which are out of the [0,255] range because at the very end we will normalized the image values.


Still under construction...
