import serial
from picamera import PiCamera
import time
import random
import datetime

#define the camera settings:
camera = PiCamera(resolution=(1920,1080))
camera.shutter_speed = 3000
camera.iso = 1600
time.sleep(1)
#you can consult https://picamera.readthedocs.io/en/release-1.13/index.html for more
#info on camera settings

#iniciate the serial communication check the RFID logger datasheet
#to get the baudrate and the other settings
ser = serial.Serial(
  
   port='/dev/ttyUSB0',#ls /dev/tty*
   baudrate = 9600,
   parity=serial.PARITY_NONE,
   stopbits=serial.STOPBITS_ONE,
   bytesize=serial.EIGHTBITS,
   timeout=1
)

#in the case of the priorityOne logger the tags are seperated by "\r"
#for example
#b'011016BA90\r011016BA90\r011016BA90\r"
#you can check how data is read by the raspberry pi with the loop
#while 1:
#    x=.readline()
#    print(x)
#In the case of priorityOne RIFDlogger we can use this function from:
#https://stackoverflow.com/questions/45215838/python-serial-pyserial-reading-lines-with-eol-r-instead-of-n?noredirect=1&lq=1
def readData():
    buffer = ""
    while True:
        oneByte = ser.read(1)
        if oneByte == b"\r":    #method should returns bytes
            return buffer
        else:
            buffer += oneByte.decode("ascii")

#loop to read from the RFIDlogger
while 1:
    x=readData()#read the data from the logger
    #print(x)
    if len(x)>9:#if the string has more than 9 characters (our tags have 10 characters)
                #take a picture. Setting up this  threshold is useful to avoid noise from
                #the serial communication
        #define the name by pasting the tag number with the date and time
        name=str(x)+"_"+str(datetime.datetime.now())[0:10]+"_"+str(datetime.datetime.now())[11:19]
        #defining the directory to save the image
        directory='/home/pi/Desktop/Photos/'+name+'.jpg'
        #take a picture and save it
        camera.capture(directory)
        #in order to increase variation in the pictures you can
        #change the camera settings for the next picture.
        #in this case we change the shutter_speed
        camera.shutter_speed = random.randint(8000,10000)
        #setup a time limit to take the next picture (to avoid identical pictures)
        time.sleep(2)
        #clear the data arriving from the RFIDlogger (as the logger reads the
        #tag every 1/3 of a second)
        ser.reset_input_buffer()
        #clear the tag variable
        x=""
    
