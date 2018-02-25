#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gpiozero import LED, LEDBoard, PWMLED
from time import sleep
from signal import pause

#Pin nubering is BCM and not BOARD numbering like in RPi.GPIO.

#led = PWMLED(17)
leds = LEDBoard(4, 17, 18, 27, 22, 23, 24, 25, 5, 6, pwm=True)  


leds.value = (0.0, 0.2, 0.0, 0.2, 0.0, 0.2, 0.0, 0.2, 0.0, 0.2)

# brightnes = 1.0
# while True:
#     led.value = brightnes
#     sleep(0.1)
    
#     if brightnes >= 0.1:
#         brightnes -= 0.1
#         brightnes = round(brightnes, 1)
#     elif brightnes == 0.0:
#         brightnes = 1.0

#     print("Brightne: ", brightnes)



pause()
