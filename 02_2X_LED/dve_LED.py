# -*- coding: utf-8 -*-

#Navodilo: Programsko kodo, ki smo jo uporabili pri povezavi ene LED diode spremeni tako, da bo mogoce svetiti z obema 



# Vkljucimo knjiznice, ki jih potrebujemo
import RPi.GPIO as GPIO
import time

Led = 11  #Ostevilcimo pin na katerem je Led1

# Funkcija z zacetnimi nastavitvami programa 
def setup():
    GPIO.setmode(GPIO.BOARD) #Nastavitev uporabe oznacevanja pinov
    GPIO.setup(Led, GPIO.OUT) #Nacin priklopa (pina) na izhod.
    GPIO.output(Led, GPIO.HIGH) #Nastavi visok izhod (3.3V) za izklop zarnice.

# Funkcija z neskoncno zanko kjer krmilimo vklop in izklop LED diode.
def loop():
    while True:
        print ("... Led prizgana")     # Izpis v ukazno vrstico.
        GPIO.output(Led, GPIO.LOW)     # Led prizgana.
        time.sleep(0.3)                 # Pocakaj pol sekunde.
        print ("... Led ugasnjena")    
        GPIO.output(Led, GPIO.HIGH)    # Led ugasnjena
        time.sleep(0.3)

# Funkcija ugasne vsa stikala na GPIO vezju. 
def destroy():
    GPIO.output(Led, GPIO.HIGH) # Led1 off
    GPIO.cleanup()

if __name__ == '__main__':    #Zacetek glavnega programa. 
    setup()
    try:
        loop()
    except KeyboardInterrupt: #Pritisni ctrl+c za koncanje programa
        destroy()

        
