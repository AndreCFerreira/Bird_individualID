## Training 

In order to train a model to select the region occupied by a specific object of interest in an image you need a dataset of images with the spatial information on the region of interest. To archive that you can manually annotate few hundred pictures with the object of interest using an annotation software such as [VGG](http://www.robots.ox.ac.uk/~vgg/software/via/via-1.0.6.html) (Dutta, A., & Zisserman, A. (2019). The VGG image annotator (VIA). arXiv preprint arXiv:1904.10699).

Upload the training images to VGG, by clicking on Image -> load or add images. The number of images needed for training depends on the complexity of the problem. Since this task requires manual work, in order to avoid spending too much time labelling regions of interest start by uploading 100-200 pictures. If the results are not satisfactory you can add more pictures later.

To start labelling the regions of interest select Regions Attributes and add a new column by writing the name of the column (in the image example we chose “name”). Select Polyline shape in the Region Shape and start selecting the region of interest by clicking with the left mouse click (in the image example we selected the head of the bird) and give a name to the delimited region (in the example “head”).

<img src="https://github.com/AndreCFerreira/Weaver_individualID/blob/master/Data_pre-processing/Training_model/Images/VGG_example.png" width="648" height="432" />


After selecting the region of interest in all pictures go to Annotation->save JSON to download the file which contains the information about the regions of interest. Keep this file in the same folder as the training pictures. Repeat the process for another smaller dataset which will be used as validation data set.

To train the model you can use the scripts provided in [this repository](https://github.com/matterport/Mask_RCNN). Please cite XXX if using this code.

Download and extract the repository. You can use the example in the folder /PATH/TO/Mask_RCNN-master/samples/balloon to train a model on your own dataset. Open the terminal on this folder and type the following code:

```console
python3 balloon.py train --dataset=/path/to /dataset --weights=coco
```

You should have a folder (e.g. “dataset”) with two folders one for training and another for validation (“train” and “val”) with the pictures and JSON in the respective folders. By default the model will be trained for 10 epochs and store a backup of the model every epoch in the folder /PATH/TO/Mask_RCNN-master/logs/. If you want to change the number of epochs or change any of the hyperparameters, edit the python script balloon.py or consult the original [repository](https://github.com/matterport/Mask_RCNN).

After training you can evaluate the model performance using the notebook “inspect_balloon_data.ipynb” provided in this [repository](https://github.com/matterport/Mask_RCNN) and you can extract the regions of interest from the original pictures following an [this notebook]( https://github.com/AndreCFerreira/Weaver_individualID/blob/master/Data_pre-processing/Training_model/Extracting_region_of_interest.ipynb).
