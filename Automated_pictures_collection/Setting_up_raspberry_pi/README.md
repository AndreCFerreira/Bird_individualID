## Raspberry pi first steps

[Raspberry pi]( https://www.raspberrypi.org/help/what-%20is-a-raspberry-pi/) is a single-board low cost computer initially designed to promote teaching of computer science in developing countries, but has caught the interest of researchers in recent years (consult this [article](https://www.nature.com/articles/544125a.pdf?origin=ppub) for an introduction to raspberry pi and arduino).


<img src="https://github.com/AndreCFerreira/Weaver_individualID/blob/master/Automated_pictures_collection/Setting_up_raspberry_pi/Images/IMG_6313.JPG" width="648" height="432" />


In order to use a raspberry pi a microSD (minimum 16gb) needs to be formated to fat32 format (check [this site]( https://www.raspberrypi.org/documentation/installation/sdxc_formatting.md) for more information).
For the first time users of a raspberry pi, we recommend installing Raspbian operating system using [NOOBS](https://www.raspberrypi.org/downloads/). After dowloading, extract the content of the zip file to the formatted microSD card and insert it on the raspberry pi. Connect a keyboard and mouse on the USB ports of the raspberry pi, a display screen using a HDMI port and connect the raspberry pi camera on the camera slot. After loading the system check the checkbox for the raspebian operating system, click on install and confirm.


<img src="https://github.com/AndreCFerreira/Weaver_individualID/blob/master/Automated_pictures_collection/Setting_up_raspberry_pi/Images/raspbian%20installation.JPG" width="648" height="432" />

When the installation is completed you need to activate the camera opening the configuration menu

<img src="https://github.com/AndreCFerreira/Weaver_individualID/blob/master/Automated_pictures_collection/Setting_up_raspberry_pi/Images/raspberryconfig.png" width="648" height="432" />

Select the interface tab and enable the camera.

<img src="https://github.com/AndreCFerreira/Weaver_individualID/blob/master/Automated_pictures_collection/Setting_up_raspberry_pi/Images/camera.png" width="648" height="432" />

Reboot the raspberry pi and test the camera by typing in the terminal
```console
raspistill -o test.jpg
```
