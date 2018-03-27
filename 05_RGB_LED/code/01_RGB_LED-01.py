#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import RPi.GPIO as GPIO

red = 11
blue = 12
green = 13

#Inicializacija pinov za posamezni priklop
GPIO.setup(red, GPIO.OUT)
GPIO.output(red, GPIO.HIGH)
GPIO.setup(blue, GPIO.OUT)
GPIO.output(red, GPIO.HIGH)
GPIO.setup(green, GPIO.OUT)
GPIO.output(red, GPIO.HIGH)

try:

    while True:
        print ('LEDs on!')
        GPIO.output(red, GPIO.LOW)
        GPIO.output(blue, GPIO.LOW)
        GPIO.output(green, GPIO.LOW)
        time.sleep(1)
        GPIO.output(red, GPIO.HIGH)
        GPIO.output(blue, GPIO.HIGH)
        GPIO.output(green, GPIO.HIGH)
        time.sleep(1)

except KeyboardInterrupt:
    GPIO.output(red, GPIO.HIGH)
    GPIO.output(blue, GPIO.HIGH)
    GPIO.output(green, GPIO.HIGH)
	GPIO.cleanup()


