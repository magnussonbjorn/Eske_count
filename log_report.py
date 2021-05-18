#!/usr/bin/env python
#coding=utf-8

import os
import datetime
from datetime import date, timedelta
from time import sleep
import yagmail

comparison = "6:30:0"
logmail = "template@gmail.com"
logpass = "temppass"
send_to = "reciever_email"

#Returns the content of the requested file, if it exists
def read_file(args):

	if(os.path.exists("./log/"+args+str(date.today() - timedelta(days = 1))+".txt") == True):

		file = open("./log/"+args+str(date.today() - timedelta(days = 1))+".txt", "r")
		contents = file.read()
		file.close()
		return contents
	else:
		return "0"

#sends data from the logs daily
while True:

	#compares requested time with current time
	if(str(datetime.datetime.now().hour)+":"+str(datetime.datetime.now().minute)+":"+str(datetime.datetime.now().second) == comparison):

		tot_sent = read_file("tot_")
		eske_sent = read_file("eske_")
		bags = int(tot_sent) - int(eske_sent)
		relevant_date = (date.today() - timedelta(days = 1))

		if(str(tot_sent) != "0"):

			yag = yagmail.SMTP(user = logmail, password = logpass, host="smtp.gmail.com")
			subject = "Report "+str(relevant_date)
			contents = "Totalt producerat "+str(tot_sent)+" på påsbanan, varav "+str(eske_sent)+" försändelser var paket och resterande "+str(bags)+" var påsar."
			yag.send( send_to, subject, contents)



	#never end
	sleep(1)
