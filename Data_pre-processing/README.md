# Data pre-processing

There are two major steps in data pre-processing. The first step is to localize and extract the animal (or body part) for later individual identification.

### Localize and extract the regions of interest
In our paper we used Mask R-CNN following [this tutorial]( https://www.learnopencv.com/deep-learning-based-object-detection-and-instance-segmentation-using-mask-r-cnn-in-opencv-python-c/) to detect and extract sociable weavers without any additional training. However you can obtain better results by training a model to localize your specific study species or a specific body part of the animal (e.g. face) following [this tutorial]( https://github.com/AndreCFerreira/Weaver_individualID/tree/master/Data_pre-processing/Training_model).

###  Apply noise and blur transformations
The second step is to apply transformations to the images used for training either to artificially increase the sample size for training or to improve the generalization capability of the models. In our paper we used blur and noise and the you can find the code used in [this script]( https://github.com/AndreCFerreira/Weaver_individualID/blob/master/Data_pre-processing/Blur_noise_transformation.ipynb).

