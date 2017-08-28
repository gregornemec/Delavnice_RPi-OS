import RPi.GPIO as GPIO
import time

pins = [18, 22, 32, 31, 36, 33, 16, 37, 38, 40]


def setup():
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
    GPIO.output(pins[ledN], GPIO.LOW)
    #print(" ... led on", pin)

def singleLedOff(ledN):
    GPIO.output(pins[ledN], GPIO.HIGH)
    #print(" ... led off", pin)

def singleLedBlink(ledN):
    singleLedOn(ledN)
    time.sleep(0.2)
    singleLedOff(pin)
    time.sleep(0.2)
    
    print(" ... led blink", ledN)

def allOn():
    print ("... all on")
    for ledN, pin in enumerate(pins):
        singleLedOn(ledN)

def allOff():
    print ("all off ...")
    for ledN, pin in enumerate(pins):
        print(ledN, "|", pin)
        singleLedOff(ledN)
    

def allBlink():
    allOn()
    time.sleep(0.2)
    allOff()
    time.sleep(0.2)

def tripleBlink():
    for i in range(0,3):
        time.sleep(0.2)
        allBlink()

def flowLed():
    print ("... flow LED ...")
    allOff()
    for ledN, pin in enumerate(pins):
        singleLedOn(ledN)
        time.sleep(0.2)
        singleLedOff(ledN)

def listLedOnOff(switches):
    '''swiches is a bit list [1, 1, 1, 0, 0, 0]. Each bit in turns on (1) or turns of (0) led light in a row.

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
    allOff()
    GPIO.cleanup()                     # Release resource

