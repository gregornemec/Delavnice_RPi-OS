#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import RPi.GPIO as GPIO

# Shranjevanje posameznih priklopov LED na GPIO v seznamu

pins = [7, 11, 12, 13, 15, 16, 18, 22,  29, 31]

def nastavi():
    '''Nastavljanje začetnih nastavitev.'''

    GPIO.setmode(GPIO.BOARD)
    for pin in pins:
        GPIO.setup(pin, GPIO.OUT)

    ugasni_vse()

def pocisti():
    '''Pocisti za konec programa.'''
    ugasni_vse()
    GPIO.cleanup()

def prizgi_vse():
    for pin in pins:
        GPIO.output(pin, GPIO.LOW)
        print('Prizgan pin', pin)

def ugasni_vse():
    for pin in pins:
        GPIO.output(pin, GPIO.HIGH)
        print('Ugasnjen pin', pin)
try:
    nastavi()
    while True:
        # Dopolni program tako, da bodo utripale vse lučke.
        pass
except KeyboardInterrupt:
    pocisti()
