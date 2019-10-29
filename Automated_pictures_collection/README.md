# Automated system for pictures collection

If unfamiliar to raspberry pi follow [this tutorial](https://github.com/AndreCFerreira/Weaver_individualID/tree/master/Automated_pictures_collection/Setting_up_raspberry_pi) to correctly  setup a raspberry pi and pi camera.

In order to make an RFID based camera trap, communication between the raspberry pi and the RFID logger needs to be established. In the paper we used priority one [RFID loggers](http://www.priority1design.com.au/shopfront/index.php?main_page=product_info&cPath=1&products_id=29&zenid=u8jajja1gqub656pkmc9h8d1k7) which have a RS232 communication port. Here it is explained how to setup this communication with the priority one loggers, if working with a different RFID brand the respective technical datasheet or manufacture should be consulted to understand how the logger could export the tag to an external machine.

## 1. Setup the RFID logger to export the detected tags
From reading the [technical datasheet](http://www.priority1design.com.au/rfidlog_rfid_data_logger.pdf) for the RIFD logger, it is possible to understand that this logger does not export the detected tag through the RS232 port by default (this might happen with other logger brands). Nonetheless it is possible to connect an [RS232 to USB adapter]( https://en.wikipedia.org/wiki/USB_adapter#/media/File:FTDI_USB_SERIAL.jpg) to the logger and, by using a terminal serial communication software (in our case we used [termite]( https://www.compuphase.com/software_termite.htm), we can configure the logger to export the detected tag (by following the instructions on the technical datasheet).

## 2. Establishing communication between the RFID logger and the raspberry pi
In order to make an automatic labelling camera trap, connect the RS232 to USB adaptor to the logger and to the raspberry pi’s USB port.  This will allow that the information relative to the tags being detect at the RFID logger to pass to the raspberry pi which, in turn, will take a photo through the raspberry pi cam and label it by including in the photos file's name the unique number of the detected tag. 

<p align="center">
<img src="https://github.com/AndreCFerreira/Weaver_individualID/blob/master/Automated_pictures_collection/Images/Setup_pi_camera.JPG" width="600" height="300" />
</p>

## 3. Initializing the raspberry pi
Connect the raspberry pi to a keyboard, a mouse and a screen, after powering the raspberry pi, open the terminal and type

```console
ls /dev/tty*
```
This will show the devices connected to the raspberry pi. Look for the ones that are named “/dev/ttyUSBx”. If multiple USB devices appear and it is not possible to determine which one corresponds to the RFID logger, copy all of them to a txt file for now.

<p align="center">
<img src="https://github.com/AndreCFerreira/Weaver_individualID/blob/master/Automated_pictures_collection/Images/ls_USB.png" width="600" height="300" />
</p>
 
## 4. Programing the raspberry pi to take photos
After establishing the communication between devices, the python code provided [here](https://github.com/AndreCFerreira/Weaver_individualID/blob/master/Automated_pictures_collection/RFID_camera.py) can be used and modified accordingly. The most important part is to paste the “/dev/ttyUSBx” line that was copied in the previous step in the provided script. For the case with multiple USB units, all of them should be tested (by running the script and passing an RFID tag by the logger), one at each time. This script takes pictures every time that information about a tag is sent from the RFID logger to the raspberry pi, however modifications to the code can be applied directly on the raspberry pi using Thonny python IDE which is installed by default in the Raspbian system.
 
<p align="center">
<img src="https://github.com/AndreCFerreira/Weaver_individualID/blob/master/Automated_pictures_collection/Images/Thonny_script.png" width="600" height="300" />
</p>

## 5. Start the script on boot 
Since an hdmi screen is probably not available in the places where the camera trap will be used (i.e. in the field) it is useful to program the raspberry pi to run the camera script as soon as it is powered to avoid the need to run the script manually. This can be achieved by typing on the terminal:

```console
sudo nano /etc/rc.local
```

This will open a document on the console that where it is possible to add the following in the line before “exit 0”:

```console
python3 </PATH/TO/RFID_camera.py> &
```
In the image example, the script is stored in a folder on the Desktop named “Photos”.

<p align="center">
<img src="https://github.com/AndreCFerreira/Weaver_individualID/blob/master/Automated_pictures_collection/Images/script_on_boot.png" width="600" height="300" />
</p>

 
After pasting the text, press ctrl+o and after ctrl+x. Now every time that the raspberry py is turn on it will automatically start the script to take photos without the need for a screen, mouse and keyboard. Again, it is important to make sure to have the right “/dev/ttyUSBx” pasted on the script. Please note that the USB number corresponding to the RFID logger might change after removing other USB devices, such as mouse or keyboard.

If everything worked well, the final output should have pictures that are labelled with the pit-tag code corresponding to the individual, as well as the date and any other information relevant to add. Note that the “:” on the time stamp on the files names might raise issues especially if the files are transferred to a windows computer. Files can be renamed by replacing the “:” with “-“ by typing the following code on the terminal:

```console
cd </PATH/TO/PICTURES_FOLDER >
rename 's/\:/-/g' *.jpg
```

<p align="center">
<img src="https://github.com/AndreCFerreira/Weaver_individualID/blob/master/Automated_pictures_collection/Images/images.png" width="600" height="300" />
</p>

