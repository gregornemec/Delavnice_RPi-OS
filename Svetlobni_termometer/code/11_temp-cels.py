#!/usr/bin/env python
import ADC0832
import time
import math

def init():
    ADC0832.setup()

def temp_calibretion():
    temp1 = 22.0
    res1 = 120.0

    temp2 = 28.5
    res2 = 156.0

    #k = (temp2 - temp1)/(res2 - res1)
    k = temp1/res1
    return k

def loop():
    while True:
        res = ADC0832.getResult()
        temp_c = round(res*temp_calibretion(),2)
        print("temp(C) =", temp_c)
        print("res =", res)
        time.sleep(0.2)


if __name__ == '__main__':
    init()
    try:
        loop()
    except KeyboardInterrupt:
        ADC0832.destroy()
        print 'The end !'
