# Data pre-processing

Here we show how to extract the animals from the pictures, how to apply noise and blur, how to organize the pictures files into training and validation datasets in order to use them to train the CNN and how to used the a similarity index to avoid near-identical pictures in the dataset.

### Localize and extract the regions of interest

In our paper we used Mask R-CNN following [this tutorial]( https://www.learnopencv.com/deep-learning-based-object-detection-and-instance-segmentation-using-mask-r-cnn-in-opencv-python-c/) to detect and extract sociable weavers without any additional training. However you can obtain better results by training a model to localize your specific study species or a specific body part of the animal (e.g. face) following [this tutorial]( https://github.com/AndreCFerreira/Weaver_individualID/tree/master/Data_pre-processing/Training_model).

###  Apply noise and blur transformations

The second step is to apply transformations to the images used for training either to artificially increase the sample size for training or to improve the generalization capability of the models. In our paper we used blur and noise and the you can find the code used in [this script]( https://github.com/AndreCFerreira/Weaver_individualID/blob/master/Data_pre-processing/Blur_noise_transformation.ipynb).

### Moving files

There are multiple ways to feed the picture to the CNN during training. One of the easiest is to organize the pictures of each individual in different folders. You can follow [this script]( https://github.com/AndreCFerreira/Weaver_individualID/blob/master/Data_pre-processing/Train_validation_dataset.ipynb) to automatically organize the files and split into training and validation datasets. 

### Similarity index

If you need to remove near-similar pictures from the training or validation dataset you can follow [this script](https://github.com/AndreCFerreira/Weaver_individualID/blob/master/Data_pre-processing/Image_similarity.ipynb)
