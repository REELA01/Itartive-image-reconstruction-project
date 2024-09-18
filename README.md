# Iterative Medical Image Reconstruction

## Overview

This project focuses on the implementation and evaluation of iterative medical image reconstruction algorithms. Medical imaging techniques such as CT (Computed Tomography) and MRI (Magnetic Resonance Imaging) often require precise image reconstruction methods to achieve high-quality images from raw data (sinograms, k-space data, etc.). Iterative reconstruction techniques offer significant advantages over traditional methods, such as reducing noise, improving resolution, and allowing for fewer measurements while maintaining accuracy.

## Features

### Reconstruction Methods:

* Algebraic Reconstruction Technique (ART)
* Simultaneous Iterative Reconstruction Technique (SIRT)
* Total Variation Minimization (TVM)
* Conjugate Gradient Least Squares (CGLS)
* Maximum Likelihood Expectation Maximization (MLEM)

### Data Input:
Supports different types of input data such as sinograms (CT) and k-space data (MRI).

### Visualization:
Tools for visualizing the reconstruction process and final reconstructed images.

## Prerequisites
The following dependencies are required to run the project:

* Python 3.8+
* NumPy
* Matplotlib
* Scikit-Image
