# Sobel Filter/Operator (Edge Detection)

Let's create a tool to detect edges of an image! To do so we'll use the Sobel operator/filter (there are other techniques out there, e.g. Canny edge detector). The matrices associated with the kernels we'll be using are given by:

$$
G_x = \left\[\begin{array}{cc} 
1 & 0 & -1 \\
2 & 0 & -2 \\
1 & 0 & -1
\end{array}\right\]
\quad\text{and}\quad
G_y = \left\[\begin{array}{cc} 
1 & 2 & 1 \\
0 & 0 & 0 \\
-1 & -2 & -1
\end{array}\right\]
$$ 

Think of $G_x$ and $G_y$ as maps of the form $\mathbb{R}^{3\times3}\rightarrow\mathbb{R}$, where we take in a 3 by 3 patch of image (denoted by $A\in\mathbb{R}^{3\times3}$), do some operation on it (using the matrices shown above), and return a real number (the value of the pixel for the output image). So, for example, if we are given the following patch of grayscale image:

<p align="center">
  <img src="Images/grayscale_patch.PNG" />
</p>

which is really the matrix:

$$
A = \left\[\begin{array}{cc} 
119 & 80 & 122 \\
177 & 154 & 212 \\
89 & 25 & 152
\end{array}\right\]
$$ 

Then the output from the operations is:

$$
\begin{array}{c}
G_x\(A\)=1\cdot119+0\cdot80-1\cdot122+2\cdot177+0\cdot154-2\cdot212+1\cdot89+0\cdot25-1\cdot152 \newline\newline
\therefore\quad G_x\(A\)=-136 \newline\newline
\quad\text{and}\quad\newline\newline
G_y\(A\)=1\cdot119+2\cdot80+1\cdot122+0\cdot177+0\cdot154+0\cdot212-1\cdot89-2\cdot25-1\cdot152 \newline\newline
\therefore\quad G_y\(A\)=110
\end{array}
$$

To apply the Sobel operation to that patch of image we want to calculate:

$$
\sqrt{\[G_x\(A\)\]^2+\[G_y\(A\)\]^2}
$$

which in the case of this example is equal to 174.917. This number will be the pixel contained in the output image. For now it's ok to have values which are out of the [0,255] range because at the very end we will normalize the image values. Notice that the output will be always greater than or equal to zero. We do this operation for the entire input image and create a new image based on these outputs just describe above.

This completes the application of the edge detection technique. If you are interested I have a couple of videos showing some details on YouTube:
[Sobel Filter - Part 1](https://www.youtube.com/watch?v=0oIESKKokPc) and [Sobel Filter - Part 2](https://www.youtube.com/watch?v=eifdexvpnq0).
