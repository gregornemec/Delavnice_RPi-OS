#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gpiozero
import time


#inicializacija LED
#led = gpiozero.LED(17)

#SEMAFOR P
#inicializacija semafor pešci
# p_zelena = gpiozero.LED(6)
# p_rdeca = gpiozero.LED(5)

# while True:
#     p_rdeca.on()
#     p_zelena.off()
#     time.sleep(10)

#     p_rdeca.off()
#     p_zelena.on()
#     time.sleep(3)


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

    
#inicializacija piskača
# zvok = gpiozero.Buzzer(21)

# #inicializacija gumb
# gumb = gpiozero.Button(20)


# def signal(t):
#     led.on()
#     zvok.on()
#     print("LED on")
#     time.sleep(t)
#     led.off()
#     zvok.off()
#     print("LED off")
#     time.sleep(t)


# while True:
#     if gumb.is_held:
#         signal(0.1)        
#         print("Držim")
#     else:
#         signal(1)
#         print("Ne držim")





