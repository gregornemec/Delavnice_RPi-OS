#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gpiozero
import time

#inicializacija LED diode 
led = gpiozero.LED(17) #GPIO povemo, da imamo LED priklopljeno na pinu 27.

while True:            #Zanka, ki se neskončno ponavlja.
    led.on()           #Z ukazom on() prižgemo LED.
    print("LED on")    #Izpis v ukazno vrstico ali lupino.
    time.sleep(1)      #Zaspi za čas v sekundah.
    led.off()          #Z ukazom off() ugasnemo LED.
    print("LED off")
    time.sleep(1)
