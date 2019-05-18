# Sobel Filter/Operator (Edge Detection)

Let's create a tool to detect edges of an image! To do so we'll use the Sobel operator/filter (there are other techniques out there, e.g. Canny edge detector). The matrices associated with the kernels we'll be using are given by:

<img src="https://latex.codecogs.com/gif.latex?G_x=\begin{bmatrix}&space;1&space;&&space;0&space;&&space;-1&space;\\&space;2&space;&&space;0&space;&&space;-2&space;\\&space;1&space;&&space;0&space;&&space;-1&space;\end{bmatrix}\quad\text{and}\quad&space;G_y=\begin{bmatrix}&space;1&space;&&space;2&space;&&space;1&space;\\&space;0&space;&&space;0&space;&&space;0&space;\\&space;-1&space;&&space;-2&space;&&space;-1&space;\end{bmatrix}" title="G_x=\begin{bmatrix} 1 & 0 & -1 \\ 2 & 0 & -2 \\ 1 & 0 & -1 \end{bmatrix}\quad\text{and}\quad G_y=\begin{bmatrix} 1 & 2 & 1 \\ 0 & 0 & 0 \\ -1 & -2 & -1 \end{bmatrix}" />

Think of <img src="https://latex.codecogs.com/gif.latex?G_x" /> and <img src="https://latex.codecogs.com/gif.latex?G_y" /> as maps of the form <img src="https://latex.codecogs.com/gif.latex?\mathbb{R}^{3\,\times,3}\rightarrow\mathbb{R}" />, where we take in a 3 by 3 patch of image (denoted by <img src="https://latex.codecogs.com/gif.latex?$$A\in\mathbb{R}^{3\,\times\,3$$" />), do some operation (using matrices associated with Gx and Gy), and returns a real number (the pixel value of the output).

So, for example, if we are given the following patch of grayscale image:

![alt-text](Images/grayscale_patch.PNG "Example of a grayscale patch")

which is really the following matrix:

<img src="https://latex.codecogs.com/gif.latex?A=\begin{bmatrix}&space;119&space;&&space;80&space;&&space;122&space;\\&space;177&space;&&space;154&space;&&space;212&space;\\&space;89&space;&&space;25&space;&&space;152&space;\end{bmatrix}" />

Then the output from the operations is:

<img src="https://latex.codecogs.com/gif.latex?G_x(A)=1\cdot&space;119+0\cdot&space;80-1\cdot&space;122+2\cdot&space;177+0\cdot&space;154-2\cdot&space;212+1\cdot&space;89+0\cdot&space;25-1\cdot&space;12" />
<img src="https://latex.codecogs.com/gif.latex?\therefore&space;G_x(A)=-136" />


and

<img src="https://latex.codecogs.com/gif.latex?G_x(A)=1\cdot&space;119+2\cdot&space;80+1\cdot&space;122+0\cdot&space;177+0\cdot&space;154+0\cdot&space;212-1\cdot&space;89-2\cdot&space;25-1\cdot&space;12" />
<img src="https://latex.codecogs.com/gif.latex?\therefore&space;G_y(A)=110" />

To apply the Sobel operation to that patch of image we want to calculate:

<img src="https://latex.codecogs.com/gif.latex?\sqrt{\big[G_x(A)\big]^2+\big[G_y(A)\big]^2}\quad\text{which&space;in&space;the&space;case&space;of&space;this&space;example&space;is&space;equal&space;to&space;}\,174.917" />

For now it's ok to have values which are out of the [0,255] range because at the very end we will normalized the image values.


Still under construction...
