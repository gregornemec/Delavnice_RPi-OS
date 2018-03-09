#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gpiozero
import time

led = gpiozero.LED(27)
zvok = gpiozero.Buzzer(21)


while True:
    led.on()
    zvok.on()
    print("LED on")
    time.sleep(0.5)
    led.off()
    zvok.off()
    print("LED off")
    time.sleep(0.5)




