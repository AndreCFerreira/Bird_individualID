## Requirements
Instructions given in this repository are meant to be used using a machine with a linux operating system installed (in our case we used [Ubuntu 18.04 LTS ](https://ubuntu.com/download/desktop))
We also assume that readers are already aware that deep Learning is very computationally intensive and therefore have access to a computer with the minimum requirements for their project. In our case we used a computer with 64gb RAM and a GPU nvidia RTX2070. 
We recommend installing python 3.x using [Anaconda](https://www.anaconda.com/distribution/). It is useful to work with anaconda python as it allows creating conda isolated environments that can contain different versions of Python and/or installed packages. 
After installing python a conda environment named “individualID” can create a conda environment by typing in Linux terminal.
```console
conda create -n individualID python=3.6
```
You can then activate the conda environment by typing:
```console
source activate individualID
```
After activating the virtual environment you should install jupyter notebook which is an interactive computing environment that enables users to easily create, edit and share documents that containing code. By typing in the linux terminal
```console
pip install jupyter notebook
```
After installing jupyter you can open any jupyter notebook scripts presented in this repository by going to the notebook’s directory, activating the virtual environment and typing jupyter notebook 
```console
cd <PATH/TO/NOTEBOOK>
source activate individualID
jupyter notebook
```
Installing tensorflow and keras (the modules needed to train a convolutional neural network) can be troublesome as you need to properly install the graphic cards drives, [CUDA]( https://developer.nvidia.com/cuda-zone), [cuDNN](https://developer.nvidia.com/cudnn) and other dependencies. However there are many helpful guides that can be greatly facility the process (some examples: [here]( https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html?source=post_page---------------------------), [here](https://medium.com/@vitali.usau/install-cuda-10-0-cudnn-7-3-and-build-tensorflow-gpu-from-source-on-ubuntu-18-04-3daf720b83fe) and [here]( https://www.pyimagesearch.com/2019/01/30/ubuntu-18-04-install-tensorflow-and-keras-for-deep-learning/)). Be sure to install tensorflow version that is compatible with your CUDA and cuDNN versions, to install the right CUDA version for your graphic card and to install tensorflow on the virtual environment that you have created.

