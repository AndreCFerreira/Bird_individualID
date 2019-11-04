## Requirements
Instructions given in this repository are meant to be used in a machine equiped with a linux operating system (in our case we used [Ubuntu 18.04 LTS ](https://ubuntu.com/download/desktop)).
Readers should be aware that deep Learning is very computationally intensive and therefore should have access to a computer with the minimum requirements for their project. In our case we used a computer with 64gb RAM and a GPU nvidia RTX2070. You can consult this [guide]( https://timdettmers.com/2018/12/16/deep-learning-hardware-guide/) in order to understand the requirements for using deep learning.
 
 ## Installing python

We recommend installing python 3.x using [Anaconda](https://www.anaconda.com/distribution/). It is useful to work with anaconda python as it allows creating conda isolated environments that can contain different versions of Python and/or installed packages (avoiding potential incompatibilities).

## Creating a virtual environment

1. After installing python using conda, a conda environment should be created and named, for example, “individualID” by typing in a Linux terminal.
```console
conda create -n individualID python=3.6
```
2. A conda environment needs to be activated by typing in the linux terminal:
```console
source activate individualID
```
3. After activating the virtual environment, create a jupyter notebook, which is an interactive computing environment that enables users to easily create, edit and share documents that containing code, by typing in the linux terminal:
```console
pip install jupyter notebook
```
4. After installing jupyter, any jupyter notebook scripts presented in this repository can be acessed by going to the notebook’s directory, activating the virtual environment and typing jupyter notebook: 
```console
cd <PATH/TO/NOTEBOOK>
source activate individualID
jupyter notebook
```
## Installing modules

Installing the modules needed to train a convolutional neural network ([tensorflow](https://www.tensorflow.org/) and [keras](https://keras.io/)), can be troublesome as it is required to properly install the graphic cards drives, [CUDA]( https://developer.nvidia.com/cuda-zone), [cuDNN](https://developer.nvidia.com/cudnn) and other dependencies. However there are many helpful guides that can greatly facilitate the process (some examples: [here]( https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html?source=post_page---------------------------), [here](https://medium.com/@vitali.usau/install-cuda-10-0-cudnn-7-3-and-build-tensorflow-gpu-from-source-on-ubuntu-18-04-3daf720b83fe) and [here]( https://www.pyimagesearch.com/2019/01/30/ubuntu-18-04-install-tensorflow-and-keras-for-deep-learning/)). Special caution should be taken to install a tensorflow version that is compatible with the machine's CUDA and cuDNN versions, to install the right CUDA version for the machine's graphic card and to install tensorflow on the created virtual environment.

All other modules  are easier to install by typing on the linux terminal after activating the environment:
```console
pip install <name of the module>
```

## Python

Although all scripts used in this repository are of basic python code, if completely unfamiliarised with python a useful familiarization  with python basic knowledge, can be of great use (more specifically: [syntax]( https://www.w3schools.com/python/python_syntax.asp), [for loops]( https://www.w3schools.com/python/python_for_loops.asp) and [functions]( https://www.w3schools.com/python/python_functions.asp)).


