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


delay = 1
while True:
    if gumb.is_pressed:
        delay = 0.1
        print("Gumb")
    else:
        delay = 1
    led.on()
    zvok.on()
    print("LED on")
    time.sleep(delay)
    led.off()
    zvok.off()
    print("LED off")
    time.sleep(delay)




