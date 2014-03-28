#!/usr/bin/python
# -*- coding: utf-8 -*-
# *******************************shutdownPi*******************************
# 28.03.2014 Selim Olcer 
# 

import time
import RPi.GPIO as GPIO
import os


def shutdown(buton):
	print "bye bye..."
	os.system("sudo shutdown -h now")


		
buton = 11										#Buton'un baglanacagi pin numarasi
GPIO.setmode(GPIO.BOARD)
GPIO.setup(buton,GPIO.IN,pull_up_down = GPIO.PUD_UP)				#buton'u input olarak tan�ml�yorum. Pull up direncini aktif ediyorum.
GPIO.add_event_detect(buton, GPIO.FALLING, callback=shutdown, bouncetime=200)	#dusen kenarda 200ms bekleyip shutdown fonksiyonuna gidiyor
while True:
	time.sleep(.2)								#sonsuz dongu
