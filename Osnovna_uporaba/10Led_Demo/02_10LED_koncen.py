#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import RPi.GPIO as GPIO

# Shranjevanje posameznih priklopov LED na GPIO v seznamu

pins = [7, 11, 13, 15, 12, 16, 18, 29]

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


def prizgi_LED(n):
    '''Prizge n-to led v seznamu.'''
    if n < len(pins):
        GPIO.output(pins[n], GPIO.LOW)
    else:
        print(n, "presega stevilo priklopljenih luck.")


def ugasni_LED(n):
    '''Ugasne n-to led v seznamu.'''
    if n < len(pins):
        GPIO.output(pins[n], GPIO.HIGH)
    else:
        print(n, "presega stevilo priklopljenih luck.")


def tekoce_LED_naprej():
    for n in range(len(pins)-1):
        prizgi_LED(n)

        time.sleep(0.2)
        ugasni_LED(n)
        ugasni_LED(n+1)

try:
    nastavi()
    while True:
        # Dopolni program tako, da bodo utripale vse lučke.
        tekoce_LED_naprej()
        time.sleep(0.2)
        prizgi_vse()
        time.sleep(0.1)
        ugasni_vse()
except KeyboardInterrupt:
    pocisti()
