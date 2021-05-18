#!/usr/bin/env python
#coding=utf-8

from datetime import date, timedelta
import os
import RPi.GPIO as GPIO
from time import sleep

#Reads input from SICK
GPIO.setmode(GPIO.BCM)
INPUT_PIN = 17
GPIO.setup(INPUT_PIN, GPIO.IN)



#Reads contents of file
def read_file(date):

	file = open("./log/eske_"+str(date)+".txt", "r")
	contents = file.read()
	file.close()
	return contents

#Writes contents to file
def write_to_file(contents):

	file = open("./log/eske_"+str(date.today())+".txt", "w+")
	file.write(str(contents))
	file.close()

#Adds input to the total sum, if file does not exist it creates a new one
def input_active(args):

	if (os.path.exists("./log/eske_"+str(date.today())+".txt") == True):

		counter = int(read_file(date.today())) + 1
		write_to_file(counter)

	else:
		counter = 1
		write_to_file(counter)

#Waits for SICK input
GPIO.add_event_detect(INPUT_PIN, GPIO.RISING, callback=input_active, bouncetime = 2000)


#Constant check
while True:

	sleep(1)
