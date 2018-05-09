#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import RPi.GPIO as GPIO

# Shranjevanje posameznih priklopov LED na GPIO v seznamu

pins = []

def nastavi():
    '''Nastavljanje začetnih nastavitev.'''

    GPIO.setmode(GPIO.BOARD)
    for pin in pins:
        GPIO.output(pin, GPIO.HIGH)
        print('Ugasnjen pin', pin)

def pocisti():
    '''Pocisti za konec programa.'''
    for pin in pins:
        GPIO.output(pin, GPIO.HIGH)
        print('Ugasnjen pin', pin)
    GPIO.cleanup()

def prizgi_vse():
    '''Fukcija prizge vse LED diode, ki so podane v seznamu'''


try:
    # Zapišemo glavni del programa

except KeyboardInterrupt:
    pocisti()
