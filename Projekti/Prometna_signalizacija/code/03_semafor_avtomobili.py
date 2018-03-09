#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gpiozero
import time

#SEMAFOR AVTOMOBILI
#Inicializacija
a_zelena = gpiozero.LED(17)
a_oranzna = gpiozero.LED(27)
a_rdeca = gpiozero.LED(22)

while True:
    a_rdeca.on()
    a_oranzna.off()
    a_zelena.off()
    time.sleep(3)

    a_oranzna.on()
    time.sleep(1)

    a_rdeca.off()
    a_oranzna.off()
    a_zelena.on()
    time.sleep(3)

    a_oranzna.on()
    a_zelena.off()
    time.sleep(1)



        
