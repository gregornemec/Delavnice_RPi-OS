#!/usr/bin/env python

import os
import ADC0832
import multiLED
import RPi.GPIO as GPIO
import time
import math
from decimal import *


def init():
    GPIO.setmode(GPIO.BOARD)        # Numbers GPIOs by physical location
    ADC0832.setup()

    #PWM pin settings
    GPIO.setup(7, GPIO.OUT)
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(12, GPIO.OUT)


if __name__ == '__main__':
    init()
    try:
        light = 0.0
        p7 = GPIO.PWM(7, 25)
        p11 = GPIO.PWM(11, 50)
        p12 = GPIO.PWM(12, 75)

        p7.start(1)
        p11.start(1)
        p12.start(1)

        while True:
            dat = ADC0832.getResult()
            light = round((Decimal(dat)/255)*100, 2)
            os.system('clear')
            print("light(delez):", light)
            print("data:", dat)
            print("res:", dat*39)
            p7.ChangeDutyCycle(light)
            p11.ChangeDutyCycle(light)
            p12.ChangeDutyCycle(light)

            time.sleep(0.2)

    except KeyboardInterrupt:
        p7.stop()
        p11.stop()
        p12.stop()

        GPIO.cleanup()
        print("The end !")
