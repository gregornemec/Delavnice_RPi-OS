#!/usr/bin/env python
# -*- coding: utf-8 -*-


import RPi.GPIO as GPIO
import time

ADC_CS  = 40 #Green
ADC_CLK = 38 #Orange
ADC_DIO = 37 #Purple

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)    #Number GPIOs by its physical location
    GPIO.setup(ADC_CS, GPIO.OUT)
    GPIO.setup(ADC_CLK, GPIO.OUT)
    
def destroy():
    GPIO.cleanup()

def getResult():     # get ADC result
    GPIO.setup(ADC_DIO, GPIO.OUT)
    GPIO.output(ADC_CS, 0)

    GPIO.output(ADC_CLK, 0)
    GPIO.output(ADC_DIO, 1);  time.sleep(0.000002)
    GPIO.output(ADC_CLK, 1);  time.sleep(0.000002)
    GPIO.output(ADC_CLK, 0)

    GPIO.output(ADC_DIO, 1);  time.sleep(0.000002)
    GPIO.output(ADC_CLK, 1);  time.sleep(0.000002)
    GPIO.output(ADC_CLK, 0)

    GPIO.output(ADC_DIO, 0);  time.sleep(0.000002)

    GPIO.output(ADC_CLK, 1)
    GPIO.output(ADC_DIO, 1);  time.sleep(0.000002)
    GPIO.output(ADC_CLK, 0)
    GPIO.output(ADC_DIO, 1);  time.sleep(0.000002)

    dat1 = 0
    for i in range(0, 8):
        GPIO.output(ADC_CLK, 1);  time.sleep(0.000002)
        GPIO.output(ADC_CLK, 0);  time.sleep(0.000002)
        GPIO.setup(ADC_DIO, GPIO.IN)
        dat1 = dat1 << 1 | GPIO.input(ADC_DIO)  # or ?
        #print ("dat1:", dat1)

    dat2 = 0
    for i in range(0, 8):
        dat2 = dat2 | GPIO.input(ADC_DIO) << i
        #print ("dat2:", dat2)
        GPIO.output(ADC_CLK, 1);  time.sleep(0.000002)
        GPIO.output(ADC_CLK, 0);  time.sleep(0.000002)


    GPIO.output(ADC_CS, 1)
    GPIO.setup(ADC_DIO, GPIO.OUT)

    if dat1 == dat2:
        return dat1
    else:
        return 0

#Uporabi to funkcijo za pridobitev podatkov o temperaturi. 
def getTempResult():
    '''
    Funkcija pridobi podatke AD pretvornika in jih spremeni v stopinje celzija.

    ToDO: Potrebna je boljsa pretvorba v temperaturo, saj dejansko funkcija ni linearna. 
    '''
    temp1 = 22.0
    res1 = 120.0

    temp2 = 24
    res2 = 140.0

    k = temp2/res2

    return round(k*getResult(),2)

# def loop():
#     while True:
#         res = getResult()
#         print("res:", res)
#         time.sleep(0.4)

# if __name__ == '__main__':
#     setup()
#     try:
#         loop()
#     except KeyboardInterrupt:
#         destroy()
