#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gpiozero
import time


#Inicializacija piskača
zvok = gpiozero.Buzzer(20)
#Inicializacija gumba
gumb = gpiozero.Button(21)

while True:
    if gumb.is_pressed:
        zvok.on()
        time.sleep(0.5)
    else:
        zvok.off()
        time.sleep(0.5)



