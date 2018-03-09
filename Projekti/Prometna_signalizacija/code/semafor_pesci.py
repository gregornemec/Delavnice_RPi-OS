#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gpiozero
import time

#inicializacija semafor pešci
led = gpiozero.LED(27)

#inicializacija piskača
zvok = gpiozero.Buzzer(21)

#inicializacija gumb
gumb = gpiozero.Button(20)


def signal(t):
    led.on()
    zvok.on()
    print("LED on")
    time.sleep(t)
    led.off()
    zvok.off()
    print("LED off")
    time.sleep(t)


while True:
    if gumb.is_held:
        signal(0.1)        
        print("Držim")
    else:
        signal(1)
        print("Ne držim")





