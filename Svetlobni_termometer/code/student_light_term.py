#!/usr/bin/env python

#Uvoz drugih funkcij

import time #Knjižnica za merjenje časa. 
import RPi.GPIO as GPIO #Knjižnica za delo z GPIO vmesnikom. 
import ADC0832 #Knjižnica za pridobivanje vrednosti iz ADC0832 pretvornika.
import multiLED #Knjižnica za upravljanje z večimi LED žarnicami. 



def init():
    '''
    Nastavljanje začetnih nastavitev
    '''
    GPIO.setmode(GPIO.BOARD)        # Numbers GPIOs by physical location
    ADC0832.setup()
    multiLED.setup()

def loop():
    '''
    Glavna zanka programa. 
    '''
    while True:
        # Sem zapiši programsko kodo
        multiLED.flowLed()
        

        #temp_c = ADC0832.getTempResult()
        #print(temp_c)
        # if temp_c >= 20 and temp_c < 21:
        #     multiLED.listLedOnOff([1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        # elif temp_c >= 21 and temp_c < 22:
        #     multiLED.listLedOnOff([1, 1, 0, 0, 0, 0, 0, 0, 0, 0])



if __name__ == '__main__':
    init() #Zagon 
    try:
        loop()
    except KeyboardInterrupt:
        #ADC0832.destroy()
        multiLED.destroy()     
        print("The end !")


