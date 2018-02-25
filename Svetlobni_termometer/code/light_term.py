#!/usr/bin/env python
import os
import ADC0832
import multiLED
import RPi.GPIO as GPIO
import time
import math


def init():
    GPIO.setmode(GPIO.BOARD)        # Numbers GPIOs by physical location
    ADC0832.setup()
    multiLED.setup()


def temp_calibretion():
    temp1 = 22.0
    res1 = 120.0

    temp2 = 24
    res2 = 140.0

    k = temp2/res2

    return k

def loop():
    while True:
        dat = ADC0832.getResult()
        temp_c = round(dat*temp_calibretion(),2)
        os.system('clear')      
        print("temp(C):", temp_c)
        print("data:", dat)
        print("res:", dat*39)

        if temp_c >= 20 and temp_c < 21:
            multiLED.listLedOnOff([1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        elif temp_c >= 21 and temp_c < 22:
            multiLED.listLedOnOff([1, 1, 0, 0, 0, 0, 0, 0, 0, 0])
        elif temp_c >= 22 and temp_c < 23:
            multiLED.listLedOnOff([1, 1, 1, 0, 0, 0, 0, 0, 0, 0])
        elif temp_c >= 23 and temp_c < 24:
            multiLED.listLedOnOff([1, 1, 1, 1, 0, 0, 0, 0, 0, 0])
        elif temp_c >= 24 and temp_c < 25:
            multiLED.listLedOnOff([1, 1, 1, 1, 1, 0, 0, 0, 0, 0])
        elif temp_c >= 25 and temp_c < 26:
            multiLED.listLedOnOff([1, 1, 1, 1, 1, 1, 0, 0, 0, 0])
        elif temp_c >= 26 and temp_c < 27:
            multiLED.listLedOnOff([1, 1, 1, 1, 1, 1, 1, 0, 0, 0])
        elif temp_c >= 27 and temp_c < 28:
            multiLED.listLedOnOff([1, 1, 1, 1, 1, 1, 1, 1, 0, 0])
        elif temp_c >= 28 and temp_c < 29:
            multiLED.listLedOnOff([1, 1, 1, 1, 1, 1, 1, 1, 1, 0])
        elif temp_c >= 29 and temp_c < 30:
            multiLED.listLedOnOff([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
        else:
            multiLED.listLedOnOff([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        #allOn()

        time.sleep(0.5)

if __name__ == '__main__':
    init()
    try:
        
        loop()
        # while True:
        #     multiLED.listLedOnOff([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
        #     time.sleep(0.5)
        #     multiLED.listLedOnOff([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        #     time.sleep(0.5)
    except KeyboardInterrupt:
        #ADC0832.destroy()
        multiLED.destroy()
        #ADC0832.destroy()
        print("The end !")
