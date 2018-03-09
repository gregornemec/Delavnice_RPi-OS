#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gpiozero
import time

#inicializacija semafor pešci
p_zelena = gpiozero.LED(5)
p_rdeca = gpiozero.LED(6)

 # V zanko zapiši delovanje semaforja v naslednjih korakih: 
 # rdeča prižgana
 # zelena ugasnjena
 # počakaj 3 s

 # rdeča ugasnjena
 # zelena prižgana
 # počakaj 1 s

while True: 
    p_rdeca.on()
    p_zelena.off()
    time.sleep(3)

    p_rdeca.off()
    p_zelena.on()
    time.sleep(1)
