# Automated system for pictures collection

If you are unfamiliar to raspberry pi please start by reading [this tutorial]( https://github.com/AndreCFerreira/Weaver_individualID/new/master/Automated_pictures_collection) to correctly setup a raspberry pi and pi camera.

In order to make an RFID based camera trap communication between the raspberry pi and the RFID logger needs to be established. In the paper we used priority one [RFID loggers](http://www.priority1design.com.au/shopfront/index.php?main_page=product_info&cPath=1&products_id=29&zenid=u8jajja1gqub656pkmc9h8d1k7) which have a RS232 communication port. Here I will explain how to setup this communication with the priority one loggers but if working with a different RFID brand you should read the technical datasheet or contact your manufacture to understand how the logger could export the tag to an external computer.

# Step 1) setup the RFID logger to export the detected tags.

From reading the [technical datasheet]( http://www.priority1design.com.au/rfidlog_rfid_data_logger.pdf) 


