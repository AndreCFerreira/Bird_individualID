## Training a model to extract a region of interest

In order to train a model to select in an image the region occupied by a specific animal or body part of interest a dataset of images with the spatial information on the region of interest is needed. To achieve this, it is possible to manually annotate few hundred pictures with the delimited region of interest using an annotation software such as [VGG](http://www.robots.ox.ac.uk/~vgg/software/via/via-1.0.6.html) (Dutta, A., & Zisserman, A. (2019). The VGG image annotator (VIA). arXiv preprint arXiv:1904.10699).

Upload the training images to VGG, by clicking on "Image" -> "Load or add images". The number of images needed for training will depend on the complexity of the classification problem. Since this task requires manual work, in order to avoid spending too much time labelling regions of interest, start by uploading 100-200 pictures. If the results are not satisfactory add more pictures to the training dataset.

To start labelling the regions of interest select "Regions Attributes" and add a new column by writing the name of the column (in the image example we chose “name”). Select "Polyline Shape" in the "Region Shape" and start selecting the region of interest by clicking with the left mouse click and give a name to the delimited region.

<img src="https://github.com/AndreCFerreira/Weaver_individualID/blob/master/Data_pre-processing/Training_model/Images/VGG_great_tit.png" width="960" height="430" />


After selecting the region of interest in all pictures, go to "Annotation"-"Save JSON" to download the file which contains the information about the regions of interest. Keep this file in the same folder as the training pictures. Repeat the process for another smaller dataset which will be used as validation dataset.

To train the model use the scripts provided in [this repository](https://github.com/matterport/Mask_RCNN).

To download and extract the repository, use the example in the folder "/PATH/TO/Mask_RCNN-master/samples/balloon" to train a model on manually annotated dataset. Open the terminal on this folder and type the following code:

```console
python3 balloon.py train --dataset=/path/to /dataset --weights=coco
```

To train the model there should a folder (e.g. “dataset”) with two sub-folders one for training and another for validation datasets (“train” and “val”) with the pictures and JSON in the respective sub-folders. By default the model will be trained for 10 epochs and store a backup of the model every epoch in the folder "/PATH/TO/Mask_RCNN-master/logs/". It is possible to change the number of epochs or change any of the hyperparameters, by editing the python script "balloon.py" (consult the original [repository](https://github.com/matterport/Mask_RCNN) for more information).

After training the model performance can be evaluate by using the notebook “inspect_balloon_data.ipynb” provided in this [repository](https://github.com/matterport/Mask_RCNN), whereas to extract the regions of interest from the original pictures follow [this notebook]( https://github.com/AndreCFerreira/Weaver_individualID/blob/master/Data_pre-processing/Training_model/Extracting_region_of_interest.ipynb).
