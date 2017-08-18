#Navodilo: Sestavi vezje in zazeni program. 


# Vkljucimo knjiznice, ki jih potrebujemo
import RPi.GPIO as GPIO
import time

Led1 = 11  #Ostevilcimo pin na katerem je Led1
Led2 = 13

# Funkcija z zacetnimi nastavitvami programa 
def setup():
    GPIO.setmode(GPIO.BOARD) #Nastavitev uporabe oznacevanja pinov

    GPIO.setup(Led1, GPIO.OUT) #Nacin priklopa (pina) na izhod.
    GPIO.output(Led1, GPIO.HIGH) #Nastavi visok izhod (3.3V) za izklop zarnice.

    GPIO.setup(Led2, GPIO.OUT) #Nacin priklopa (pina) na izhod.
    GPIO.output(Led2, GPIO.HIGH) #Nastavi visok izhod (3.3V) za izklop zarnice.


# Funkcija z neskoncno zanko kjer krmilimo vklop in izklop LED diode.
def loop():
    while True:
        print ("... Led1 prizgana")     # Izpis v ukazno vrstico.
        GPIO.output(Led1, GPIO.LOW)     # Led prizgana.
        time.sleep(1)     
        print ("... Led2 prizgana")     # Izpis v ukazno vrstico.
        GPIO.output(Led2, GPIO.LOW)     # Led prizgana.
        time.sleep(1)                 # Pocakaj pol sekunde.
        print ("... Led2 ugasnjena")    
        GPIO.output(Led1, GPIO.HIGH)    # Led ugasnjena
        time.sleep(1)  
        print ("... Led1 ugasnjena")     
        GPIO.output(Led2, GPIO.HIGH)    # Led ugasnjena


# Funkcija ugasne vsa stikala na GPIO vezju. 
def destroy():
    GPIO.output(Led1, GPIO.HIGH) # Led1 off
    GPIO.output(Led2, GPIO.HIGH) # Led1 off
    GPIO.cleanup()

if __name__ == '__main__':    #Zacetek glavnega programa. 
    setup()
    try:
        loop()
    except KeyboardInterrupt: #Pritisni ctrl+c za koncanje programa
        destroy()

        
