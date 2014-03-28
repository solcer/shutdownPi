#!/usr/bin/python
# -*- coding: utf-8 -*-
# *******************************shutdownPi*******************************
# 28.03.2014 Selim Olcer 
# deneme satir

import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.IN)

while True:
	mybutton = GPIO.input(11)			#buton degerini okuyoruz.
	if mybutton == False:
		time.sleep(.2)			#debouncing icin 0.2sn bekliyoruz
		t0 = time.clock()			#s�re tutmak i�in t0'a o anki zaman� al�yoruz.
		fark=t0
		print "Baslangic: " + str(t0) 
		while GPIO.input(11) == False:	# butona bas�l� tutuldu�u s�rece bekliyoruz
			t1 = time.clock()			#t1'e yeni zaman� al�yoruz
			if t1-fark>1 :			#
				print str(t1-t0) +"sn"
				fark=t1			#ge�en s�redeki fark� bulmak i�in fark registerini g�ncelliyorum.
		t1 = time.clock()			#t1'e yeni zaman� al�yoruz
		print "t0: "
		print t0
		print "t1: "
		print t1
		