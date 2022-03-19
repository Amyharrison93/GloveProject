from gpiozero import LED as led
import RPi.GPIO as gpio
import subprocess

defaultI2CPins = [3, 5]
defaultGPIOPins = [4, 17, 27, 22, 10, 9, 11, 5, 6, 13, 19, 26, 14, 15, 18, 23, 24, 25, 8, 7, 12, 16, 20, 21]
defaultSPIPins = [19, 21, 23, 14, 26]
defaultUARTPins = [8,10]
DefaultEEPROMPins = [27, 28]

gpio.setmode(gpio.BCM)

def gpioSetup(pinCount : int):
    '''sets used pins to to outputs
    input is an integer number of pins to setup'''
    for i in range(0, pinCount):
        gpio.setup(defaultGPIOPins[i], gpio.OUT)
        
def pinInit():
    '''initialises pin 0 value to ensure a sensor is available for read'''
    gpio.output(defaultGPIOPins[0], 1)

def setPins(pattern, pins = defaultGPIOPins):
    '''sets pins based on input pattern
    inputs are an array of 0 or 1s relating to AD0 of the sensor'''
    for i in range(0, len(pattern)):
        if pattern[i] == 1:
            gpio.output(defaultGPIOPins[i], 1)
            #print("pos {} is {} so {} is on".format(i, pattern[i], defaultGPIOPins[i]))
        else:
            gpio.output(defaultGPIOPins[i], 0)
            #print("pos {} is {} so {} is off".format(i, pattern[i], defaultGPIOPins[i]))
            