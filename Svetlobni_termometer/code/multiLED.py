import RPi.GPIO as GPIO
import time

#V seznam z stevilkami vnesemo priklopljene led diode.

pins = [3, 5, 7, 8]


def setup():
    '''
    Začente nastavitve.
    '''

    GPIO.setmode(GPIO.BOARD)        # Numbers GPIOs by physical location
    for pin in pins:
        GPIO.setup(pin, GPIO.OUT)   # Set all pins' mode is output
        GPIO.output(pin, GPIO.HIGH) # Set all pins to high(+3.3V) to off led

# def singleLedOn(pin):
#     GPIO.output(pin, GPIO.LOW)
#     print(" ... led on", pin)

# def singleLedOff(pin):
#     GPIO.output(pin, GPIO.HIGH)
#     print(" ... led off", pin)


def singleLedOn(ledN):
    '''
    Prižgemo LED na številki (zacetek: 0)
    '''
    
    GPIO.output(pins[ledN], GPIO.LOW)
    #print(" ... led on", ledN)


def singleLedOff(ledN):
    '''
    Ugasnemo LED na številki (zacetek: 0)
    '''

    GPIO.output(pins[ledN], GPIO.HIGH)
    #print(" ... led off", ledN)


def singleLedBlink(ledN):
    '''
    Utripanje LED na vneseni stevilki (zacetek: 0)
    '''

    singleLedOn(ledN)
    time.sleep(0.2)
    singleLedOff(pin)
    time.sleep(0.2)
    
    print(" ... led blink", ledN)


def allOn():
    '''
    Prizge vse lucke.
    '''
    print ("... all on")
    for ledN, pin in enumerate(pins):
        singleLedOn(ledN)

def allOff():
    '''
    Ugasne vse lucke.
    '''
    print ("all off ...")
    for ledN, pin in enumerate(pins):
        print(ledN, "|", pin)
        singleLedOff(ledN)
    

def allBlink():
    '''
    Vse lucke utripajo
    '''
    allOn()
    time.sleep(0.2)
    allOff()
    time.sleep(0.2)

def tripleBlink():
    '''
    Trojni utrip luck.
    '''
    for i in range(0,3):
        time.sleep(0.2)
        allBlink()

def flowLed():
    '''
    Putojoca lucka.
    '''
    
    print ("... flow LED ...")
    allOff()
    for ledN, pin in enumerate(pins):
        singleLedOn(ledN)
        time.sleep(0.2)
        singleLedOff(ledN)

def listLedOnOff(switches):
    '''
    SI: Funkcija sprejeme seznam swiches vrednosti 0 in 1. Vrednost 0 pomeni,
    da je LED ugasnjena in 1 da je LED prizgane. Torej nam 0 oz. 1 v seznamu
    pove ali je LED na mestu v seznamu prizgana ali ugasnjena.

    ENG: swiches is a bit list [1, 1, 1, 0, 0,
    0]. Each bit in turns on (1) or turns of (0) led light in a row.

    '''

    if len(switches) == len(pins):
        print(switches)
        for ledN, bit in enumerate(switches):
            if bit == 1:
                singleLedOn(ledN)
            else:
                singleLedOff(ledN)

        return 0
    else:
        print("Seznam z stikali ni enake velikosti kot seznam z pini.")
        return -0


def destroy():
    '''
    Pocisti vse vire. 
    '''
    allOff()
    GPIO.cleanup()                     # Release resource

