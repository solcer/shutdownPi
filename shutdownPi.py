#!/usr/bin/python
# -*- coding: utf-8 -*-
# *******************************shutdownPi*******************************
# 28.03.2014 Selim Olcer 
# 

import time
import RPi.GPIO as GPIO
import os


def shutdown(buton):
	while True:
		mybutton = GPIO.input(buton)					#buton degerini okuyoruz.
		if mybutton == False:	
			time.sleep(.2)						#debouncing icin 0.2sn bekliyoruz
			t0 = time.clock()						#süre tutmak için t0'a o anki zamaný alýyoruz.
			fark=t0
			print "Baslangic: " + str(t0) 
			while GPIO.input(buton) == False:				#butona basýlý tutulduðu sürece bekliyoruz
				t1 = time.clock()					#t1'e yeni zamaný alýyoruz
				if t1-fark>1 :					#
					print str(t1-t0) +"sn"
					fark=t1					#geçen süredeki farký bulmak için fark registerini güncelliyorum.
			t1 = time.clock()						#t1'e yeni zamaný alýyoruz
			print "t0: "
			print t0
			print "t1: "
			print t1
		
buton = 11										#Buton'un baglanacagi pin numarasi
GPIO.setmode(GPIO.BOARD)
GPIO.setup(buton,GPIO.IN,pull_up_down = GPIO.PUD_UP)				#buton'u input olarak tanýmlýyorum. Pull up direncini aktif ediyorum.
GPIO.add_event_detect(buton, GPIO.FALLING, callback=shutdown, bouncetime=200)	#dusen kenarda 200ms bekleyip shutdown fonksiyonuna gidiyor
while True:
	time.sleep(.2)								#sonsuz dongu
