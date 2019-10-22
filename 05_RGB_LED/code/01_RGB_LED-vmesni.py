#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import RPi.GPIO as GPIO

red = 11
blue = 12
green = 13

#Inicializacija pinov za posamezni priklop
GPIO.setmode(GPIO.BOARD)
GPIO.setup(red, GPIO.OUT)       # Določimo način pina na izhod.
GPIO.output(red, GPIO.HIGH)     # Napetost na pinu red ugasnemo (HIGH). 
GPIO.setup(blue, GPIO.OUT)
GPIO.output(blue, GPIO.HIGH)
GPIO.setup(green, GPIO.OUT)
GPIO.output(green, GPIO.HIGH)

try:
    #Z zanko while True ponavljamo program neskončno krat.
    while True:
        print ('\n')            # Izpiši novo vrstico.
        red01 = input('red(01):')  # Vprašaj uporabnika, vrednost 0 za ugasnjeno
                                   # in 1 za prižgano led

        #Dodaj še za modro in zeleno

     # Če je vrednost spremenljivke 0 potem naj je žarnica ugasnjena in če
        # je vrednost spremenljivke 1 naj je prižgana

        if red01 == 1:
            GPIO.output(red, GPIO.LOW)
        else:
            GPIO.output(red, GPIO.HIGH)

        #Dodaj še za modro in zeleno.


except KeyboardInterrupt:
    # Za prekinitev programa uporabi kombinacijo C-c. Ko program zazna
    # prekinitev sproži pokliče še spodnje.

    GPIO.output(red, GPIO.HIGH)  # Ugasni led
    GPIO.output(blue, GPIO.HIGH)
    GPIO.output(green, GPIO.HIGH)
    GPIO.cleanup()              # Počisti GPIO.


