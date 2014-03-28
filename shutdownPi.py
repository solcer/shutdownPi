#!/usr/bin/python
# -*- coding: utf-8 -*-
# *******************************shutdownPi*******************************
# 28.03.2014 Selim Olcer 
# 

import time
import RPi.GPIO as GPIO
import os


def shutdown(buton):
	shutdown=0
	while True:
		mybutton = GPIO.input(buton)					#buton degerini okuyoruz.
		if mybutton == False:	
			t0 = time.clock()						#s�re tutmak i�in t0'a o anki zaman� al�yoruz.
			fark=t0
			print "Baslangic: " + str(t0) 
			while GPIO.input(buton) == False:				#butona bas�l� tutuldu�u s�rece bekliyoruz
				t1 = time.clock()					#t1'e yeni zaman� al�yoruz
				if t1-t0>5 :						# kapatilacak sure
					shutdown=1					#buradan ��k�p raspberry pi yi kapat�yoruz
					break
				if t1-fark>1 :					#
					print str(t1-t0) +"sn"
					fark=t1					#ge�en s�redeki fark� bulmak i�in fark registerini g�ncelliyorum.
			t1 = time.clock()						#t1'e yeni zaman� al�yoruz
			print "t0: "
			print t0
			print "t1: "
			print t1
		if shutdown==1:							#while True'dan cikmak icin
			break
	if shutdown==1:
		print "bye bye..."
		os.system("sudo shutdown -h now")

		
buton = 11										#Buton'un baglanacagi pin numarasi
GPIO.setmode(GPIO.BOARD)
GPIO.setup(buton,GPIO.IN,pull_up_down = GPIO.PUD_UP)				#buton'u input olarak tan�ml�yorum. Pull up direncini aktif ediyorum.
GPIO.add_event_detect(buton, GPIO.FALLING, callback=shutdown, bouncetime=200)	#dusen kenarda 200ms bekleyip shutdown fonksiyonuna gidiyor
while True:
	time.sleep(.2)								#sonsuz dongu
