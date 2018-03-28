#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import RPi.GPIO as GPIO

#Vpiši številke pinov 
red = 
blue = 
green = 

#Inicializacija pinov za posamezni priklop
GPIO.setmode(GPIO.BOARD)
GPIO.setup(red, GPIO.OUT)       # Določimo način pina na izhod.
GPIO.output(red, GPIO.HIGH)     # Napetost na pinu red ugasnemo (HIGH). 
GPIO.setup(blue, GPIO.OUT)
GPIO.output(blue, GPIO.HIGH)
GPIO.setup(green, GPIO.OUT)
GPIO.output(green, GPIO.HIGH)

try:
    #Sem vpisujemo programsko kodo.
    GPIO.output(green, GPIO.LOW)


except KeyboardInterrupt:
    GPIO.output(red, GPIO.HIGH)
    GPIO.output(blue, GPIO.HIGH)
    GPIO.output(green, GPIO.HIGH)
    GPIO.cleanup()


