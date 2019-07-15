# Weaver_individualID

Implementation of the paper Individual visual identification using deep learning in wild birds link

This repository explains how to automatize collection of training pictures using RFID in birds, pre-process images and train convolutional neural networks for individual identification.
The project is organized as follow:

1)	[Automated_pictures_collection: raspberry pi communication with RFID data logger to build a camera trap with automatic labelling.](https://github.com/AndreCFerreira/Weaver_individualID/tree/master/Automated_pictures_collection)

2)	[Data_pre-processing: localize and extract birds (or the body part of interest) from the pictures](https://github.com/AndreCFerreira/Weaver_individualID/tree/master/Data_pre-processing)

3)	Train_CNN: training the convolutional neural network for individual identification

4)	Work_flow_example: applying the trained model to a situation of interest

Instructions given in this repository are meant to be used using a machine with a linux operating system installed (in our case we used [Ubuntu 18.04 LTS ](https://ubuntu.com/download/desktop) 
We also assume that readers are already aware that deep Learning is very computationally intensive and therefore have access to a computer with the minimum requirements for their project. In our case we used a computer with 64gb RAM and a GPU nvidia RTX2070. 
We recommend installing python 3.x using [Anaconda](https://www.anaconda.com/distribution/). After installing python a conda environment should be created in order to install the necessary dependences.
```
conda create -n individualID python=3.7
source activate individualID <b>tag</b>.
```

