#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import RPi.GPIO as GPIO

red = 11
blue = 12
green = 13

#Inicializacija pinov za posamezni priklop
GPIO.setmode(GPIO.BOARD)
GPIO.setup(red, GPIO.OUT)
GPIO.output(red, GPIO.HIGH)
GPIO.setup(blue, GPIO.OUT)
GPIO.output(red, GPIO.HIGH)
GPIO.setup(green, GPIO.OUT)
GPIO.output(red, GPIO.HIGH)

try:
    
    while True:
        print ('\n')
        red01 = input('red(01):')
        blue01 = input('blue(01):')
        green01 = input('green(01):')

        if red01 == 1:
            GPIO.output(red, GPIO.LOW)
        else:
            GPIO.output(red, GPIO.HIGH)

        if blue01 == 1:
            GPIO.output(blue, GPIO.LOW)
        else:
            GPIO.output(blue, GPIO.HIGH)

        if green01 == 1:
            GPIO.output(green, GPIO.LOW)
        else:
            GPIO.output(green, GPIO.HIGH)

except KeyboardInterrupt:
    GPIO.output(red, GPIO.HIGH)
    GPIO.output(blue, GPIO.HIGH)
    GPIO.output(green, GPIO.HIGH)
    GPIO.cleanup()


