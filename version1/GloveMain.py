#!/usr/bin/env python

import os
import sys
import time
sys.path.append(os.getcwd())

import MPU6050Lib as mpu
import rpiGPIOLib as gpio

def main():
    '''
    Main program function
    '''
    gpio.gpioSetup(3)
    gpio.pinInit()
    sensor1 = mpu.initSensor(0x68)
    ad0Pattern = mpu.ad0Init(3)
    ad0PatternFlip = ad0Pattern
    time.sleep(1)
    
    while True:
        for i in range(0, len(ad0Pattern)): 
            ad0PatternFlip[i] = abs(int(ad0Pattern[i]) - 1)
        
        gpio.setPins(ad0PatternFlip)
        ad0Pattern = mpu.ad0Toggle(ad0Pattern)
        
        print(ad0PatternFlip)
        result1 = mpu.readAccel(sensor1)
        result2 = mpu.readGyro(sensor1)
        #print("Accel retrurned: {}, gyro returned: {}".format(result1, result2))
        try:
            print("Accel in degrees = {}".format(mpu.radToDeg(result1)))
        except Exception as e:
            print(e)
        time.sleep(1)
        
if __name__ == "__main__":
    main()

