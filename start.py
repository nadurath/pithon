#https://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/robot/buttons_and_switches/

import RPi.GPIO as GPIO
import time
import os

#adjust for where your switch is connected
startPin = 18
recordPin = 13
GPIO.setmode(GPIO.BCM)
GPIO.setup(startPin,GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(recordPin,GPIO.IN, pull_up_down = GPIO.PUD_UP)

while True:
  #assuming the script to call is long enough we can ignore bouncing
  start_input_state = GPIO.input(18)
  record_input_state = GPIO.input(13)
  if start_input_state == False:
    #this is the script that will be called (as root)
    print "Start button pressed"
    time.sleep(0.2)
    os.system("python /home/pi/Desktop/voiceControl.py")
  elif record_input_state == False:
  	print "Record button pressed"
  	time.sleep(0.2)
  	os.system("python /home/pi/Desktop/recording.py")
