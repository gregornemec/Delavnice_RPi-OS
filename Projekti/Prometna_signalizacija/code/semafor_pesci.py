#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gpiozero
import time

led = gpiozero.LED(27)

while True:
    led.on()
    time.sleep(1)
    led.off()
    time.sleep(1)



