# Data pre-processing

Here we show how to extract the animals from the pictures, how to apply noise and blur transformations, how to organize the pictures files into training and validation datasets (in order to use them to train the CNN) and how to use the similarity index to avoid near-identical pictures in the dataset.

### Localize and extract the regions of interest

In our paper we used Mask R-CNN following [this tutorial]( https://www.learnopencv.com/deep-learning-based-object-detection-and-instance-segmentation-using-mask-r-cnn-in-opencv-python-c/) to detect and extract sociable weavers without any additional training. However you can obtain better results by training a model to localize your specific study species or specific body parts of the animal (e.g. face) following [this tutorial]( https://github.com/AndreCFerreira/Weaver_individualID/tree/master/Data_pre-processing/Training_model).

###  Apply noise and blur transformations

Transformations were applied to the images for training to artificially increase the sample size for training and improve the generalization capability of the models by applying blur and noise transformations as depicted in [this script]( https://github.com/AndreCFerreira/Weaver_individualID/blob/master/Data_pre-processing/Blur_noise_transformation.ipynb).

### Moving files

There are multiple ways to feed the pictures to the CNN during training with one of the easiest being to organize the pictures of each individual in different folders. [This script]( https://github.com/AndreCFerreira/Weaver_individualID/blob/master/Data_pre-processing/Train_validation_dataset.ipynb) can be used to automatically organize the files and split into training and validation datasets. 

### Similarity index

To remove near-similar pictures from the training or validation dataset follow [this script](https://github.com/AndreCFerreira/Weaver_individualID/blob/master/Data_pre-processing/Image_similarity.ipynb).
