#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gpiozero
import time

#SEMAFOR AVTOMOBILI
#Inicializacija semafor avtomobili
a_zelena = gpiozero.LED(17)
a_oranzna = gpiozero.LED(27)
a_rdeca = gpiozero.LED(22)

#inicializacija semafor pešci
p_zelena = gpiozero.LED(5)
p_rdeca = gpiozero.LED(6)

#Inicializacija piskača
zvok = gpiozero.Buzzer(20)
#Inicializacija gumba
gumb = gpiozero.Button(21)

def prehod():
    time.sleep(2)
    #oranzna za avtomobile
    a_zelena.off()
    a_oranzna.on()
    time.sleep(1)
    #rdeca za avtomobile
    a_oranzna.off()
    a_rdeca.on()
    time.sleep(1)
    #zelena za pesce
    p_rdeca.off()
    p_zelena.on()
    zvok.on()
    time.sleep(2)
    #rdeca za pesce
    zvok.off()
    p_zelena.off()
    time.sleep(0.5)
    p_rdeca.on()
    a_oranzna.on()
    a_rdeca.off()
    time.sleep(1)
    a_zelena.on()
    a_oranzna.off()


a_rdeca.off()
a_oranzna.off()
a_zelena.on()

p_rdeca.on()
p_zelena.off()

while True:
     if gumb.is_pressed:
         print("Pritisnil!")
         prehod()
