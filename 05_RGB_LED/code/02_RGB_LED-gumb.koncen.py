#!/usr/bin/env Pyhrn
# -*- coding: utf-8 -*-

import time
import RPi.GPIO as GPIO

red = 11
blue = 13
green = 13

# Inicializacija pinov za posamezni priklop
GPIO.setmode(GPIO.BOARD)
GPIO.setup(red, GPIO.OUT)       # Določimo način pina na izhod.
GPIO.output(red, GPIO.HIGH)     # Napetost na pinu red ugasnemo (HIGH).
GPIO.setup(blue, GPIO.OUT)
GPIO.output(blue, GPIO.HIGH)
GPIO.setup(green, GPIO.OUT)
GPIO.output(green, GPIO.HIGH)


# Inicializacija gumba
GPIO.setmode(GPIO.BOARD)
GPIO.setup(36, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(38, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# Inicializacijo dodaj se za ostala gumba


try:
    # Z zanko while True ponavljamo program neskončno krat.
    while True:
        # Preverjaj stanje gumbov
        rdec_pritisnjen = GPIO.input(36)
        zelen_pritisnjen = GPIO.input(38)
        moder_pritisnjen = GPIO.input(40)

        # Vklop rdece
        if rdec_pritisnjen == False:
            print('Rdeč je pritisnjen!')
            GPIO.output(red, GPIO.LOW)
            time.sleep(0.2)
        else:
            GPIO.output(red, GPIO.HIGH)

        # Vklop zelene
        if zelen_pritisnjen == False:
            print('Zelen je pritisnjen!')
            GPIO.output(green, GPIO.LOW)
            time.sleep(0.2)
        else:
            GPIO.output(green, GPIO.HIGH)

        # Vklop modre
        if moder_pritisnjen == False:
            print('Moder je pritisnjen!')
            GPIO.output(blue, GPIO.LOW)
            time.sleep(0.2)
        else:
            GPIO.output(blue, GPIO.HIGH)


except KeyboardInterrupt:
    # Za prekinitev programa uporabi kombinacijo C-c. Ko program zazna
    # prekinitev sproži pokliče še spodnje.

    GPIO.output(red, GPIO.HIGH)  # Ugasni led
    GPIO.output(blue, GPIO.HIGH)
    GPIO.output(green, GPIO.HIGH)
    GPIO.cleanup()              # Počisti GPIO.
