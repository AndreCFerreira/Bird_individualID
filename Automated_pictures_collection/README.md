# Automated system for pictures collection

If you are unfamiliar to raspberry pi you can read [this tutorial](https://github.com/AndreCFerreira/Weaver_individualID/tree/master/Automated_pictures_collection/Setting_up_raspberry_pi) to correctly setup a raspberry pi and pi camera.

In order to make an RFID based camera trap, communication between the raspberry pi and the RFID logger needs to be established. In the paper we used priority one [RFID loggers](http://www.priority1design.com.au/shopfront/index.php?main_page=product_info&cPath=1&products_id=29&zenid=u8jajja1gqub656pkmc9h8d1k7) which have a RS232 communication port. Here it is explained how to setup this communication with the priority one loggers but if working with a different RFID brand you should read the technical datasheet or contact your manufacture to understand how the logger could export the tag to an external machine.

## Step 1) setup the RFID logger to export the detected tags.
From reading the [technical datasheet](http://www.priority1design.com.au/rfidlog_rfid_data_logger.pdf) it is possible to understand that this logger do not export the detected tag through the RS232 port by default (this might happen with other logger brands). Following the technical datasheet information it is possible to connect an [RS232 to USB adapter]( https://en.wikipedia.org/wiki/USB_adapter#/media/File:FTDI_USB_SERIAL.jpg) to the logger and using a terminal serial communication software (in our case we used [termite]( https://www.compuphase.com/software_termite.htm) we can configure the logger to export the detected tag following the instructions on the technical datasheet.

## Step 2) Establishing communication between the RFID logger and the raspberry pi
In order to make an automatic labelling camera trap the information about the tags being detect at the RFID logger needs to pass to the raspberry pi which will take the photo and label it by including the photos file name the unique number of the detected tag. 
Connect the RS232 to USB adaptor to the logger and to the raspberry pi’s USB port. 

<p align="center">
<img src="https://github.com/AndreCFerreira/Weaver_individualID/blob/master/Automated_pictures_collection/Images/Setup_pi_camera.JPG" width="600" height="300" />
</p>

Connect the raspberry pi to a keyboard, a mouse and a screen. After powering the raspberry pi open the terminal and type

```console
ls /dev/tty*
```
This will show you the devices connected to the raspberry pi. Look for the ones that are named “/dev/ttyUSBx”. If multiple USB devices appear and you do not know which one corresponds to the RFID logger copy all of them to a txt file.

<p align="center">
<img src="https://github.com/AndreCFerreira/Weaver_individualID/blob/master/Automated_pictures_collection/Images/ls_USB.png" width="600" height="300" />
</p>
 

## Step 3) Programing the raspberry pi to take photos
After establishing the communication, you can use the python coded provided [here](https://github.com/AndreCFerreira/Weaver_individualID/blob/master/Automated_pictures_collection/RFID_camera.py) and modify according to your needs. The most important part is to paste the “/dev/ttyUSBx” line that you copied in the previous step. If you have multiple USB units and you are not sure which one corresponds to the RFID logger try all of them, one at each time. This script takes pictures every time that information about a tag is sent from the RFID logger to the raspberry pi. You can modify the code directly on your raspberry pi using Thonny python IDE which is installed by default in the Raspbian system.
 
<p align="center">
<img src="https://github.com/AndreCFerreira/Weaver_individualID/blob/master/Automated_pictures_collection/Images/Thonny_script.png" width="600" height="300" />
</p>

## Step 4) Start the script on boot 
Since an hdmi screen is probably not available in the places where the camera trap will be used (i.e. in the field) it is useful to program the raspberry pi to run the camera script as soon as it is powered. This can be archived by typing on the terminal:

```console
sudo nano /etc/rc.local
```

This will open a document on the console that where you can add in the line before “exit 0”

```console
python3 </PATH/TO/RFID_camera.py> &
```

<p align="center">
<img src="https://github.com/AndreCFerreira/Weaver_individualID/blob/master/Automated_pictures_collection/Images/script_on_boot.png" width="600" height="300" />
</p>

In the image example the script is stored in a folder on the Descktop names “Photos”
 
After pasting the text, press ctrl+o and after ctrl+x. Now every time that the raspberry py is turn on it will automatically start the script to take photos. Be sure to have the right “/dev/ttyUSBx” pasted on the script. Please note that USB number corresponding to the RFID logger might change after removing USB devices such as mouse and keyboard.

If everything worked well you should have pictures that are labelled with the pit-tag code corresponding to the bird as well as the date and any other information that you might find relevant to add. Note that the “:” on the time stamp on the files names might raise issues especially if the files are transfer to a windows computer. You can rename the names by replacing the “:” with “-“. By typing the following code on the terminal:

```console
cd </PATH/TO/PICTURES_FOLDER >
rename 's/\:/-/g' *.jpg

<p align="center">
<img src="https://github.com/AndreCFerreira/Weaver_individualID/blob/master/Automated_pictures_collection/Images/images.png" width="600" height="300" />
</p>

