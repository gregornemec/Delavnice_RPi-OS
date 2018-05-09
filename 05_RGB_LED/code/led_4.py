#Navodilo: Sestavi vezje in zazeni program. 


# Vkljucimo knjiznice, ki jih potrebujemo
import RPi.GPIO as GPIO
import time

Led1 = 11  #Ostevilcimo pin na katerem je Led1
Led2 = 13

led_lucke = [15, 12, 11, 13]

# Funkcija z zacetnimi nastavitvami programa 
def setup():
    GPIO.setmode(GPIO.BOARD) #Nastavitev uporabe oznacevanja pinov


    for led in led_lucke:
        GPIO.setup(led, GPIO.OUT) #Nacin priklopa (pina) na izhod.
        GPIO.output(led, GPIO.HIGH) #Nastavi visok izhod (3.3V) za izklop zarnice.


# Funkcija z neskoncno zanko kjer krmilimo vklop in izklop LED diode.
def loop():
    while True:
        for led in led_lucke:
            GPIO.output(led,GPIO.LOW)
            time.sleep(0.1)
            GPIO.output(led,GPIO.HIGH)
            

# Funkcija ugasne vsa stikala na GPIO vezju. 
def destroy():
    for led in led_lucke:
        GPIO.output(led, GPIO.HIGH) #Nastavi visok izhod (3.3V) za izklop zarnice
    GPIO.cleanup()

if __name__ == '__main__':    #Zacetek glavnega programa. 
    setup()
    try:
        loop()
    except KeyboardInterrupt: #Pritisni ctrl+c za koncanje programa
        destroy()

        
