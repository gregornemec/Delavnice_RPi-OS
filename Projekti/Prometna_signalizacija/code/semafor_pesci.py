#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gpiozero
import time


#inicializacija LED

#inicializacija semafor pešci
pesci_zelena = gpiozero.LED(5)
pesci_rdeca = gpiozero.LED(6)

while True:
    pesci_rdeca.on()
    pesci_zelena.off()
    time.sleep(3)

    pesci_rdeca.off()
    pesci_zelena.on()
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





