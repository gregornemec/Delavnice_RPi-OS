#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gpiozero
import time

led = gpiozero.LED(27)
zvok = gpiozero.Buzzer(21)


while True:
    led.on()
    print("LED on")
    time.sleep(1)
    led.off()
    print("LED off")
    time.sleep(1)




