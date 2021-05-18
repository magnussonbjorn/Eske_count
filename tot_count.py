#!/usr/bin/env python
#coding=utf-8

from datetime import date, timedelta
import os
import RPi.GPIO as GPIO
from time import sleep

#Define GPIO input
GPIO.setmode(GPIO.BCM)
INPUT_PIN = 27
GPIO.setup(INPUT_PIN, GPIO.IN)

#Returns contents of file
def read_file(date):

	file = open("./log/tot_"+str(date)+".txt", "r")
	contents = file.read()
	file.close()
	return contents

#Writes contents to file
def write_to_file(contents):

	file = open("./log/tot_"+str(date.today())+".txt", "w+")
	file.write(str(contents))
	file.close()

#Adds the input to the total sum of the day, if file doesnt exists it creates a new one
def tot_input(args):

	if(os.path.exists("./log/tot_"+str(date.today())+".txt") == True):

		sum_of_packages = int(read_file(date.today())) + 1
		write_to_file(sum_of_packages)

	else:

		sum_of_packages = 1
		write_to_file(sum_of_packages)


#Waiting for input
GPIO.add_event_detect(INPUT_PIN, GPIO.FALLING, callback = tot_input, bouncetime = 3000)

#Constant check
while True:

	sleep(1)
