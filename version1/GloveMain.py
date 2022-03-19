#!/usr/bin/env python

import os
import sys
import time
sys.path.append(os.getcwd())

import MPU6050Lib as mpu
import rpiGPIOLib as gpio
#import GraphOutLib as graph

def main():
    '''
    Main program function
    '''
    #graph.TestPlot()
    gpio.gpioSetup(3)
    gpio.pinInit()
    
    ad0Pattern = mpu.ad0Init(3)
    ad0PatternFlip = mpu.ad0Init(3)
    
    for i in range(0, len(ad0PatternFlip)):
        ad0PatternFlip[i] = abs(int(ad0PatternFlip[i]) - 1)
    gpio.setPins(ad0PatternFlip)
    
    time.sleep(0.1)
    
    sensor1 = mpu.initSensor(0x68)
    print(sensor1)
    
    time.sleep(0.1)
    
    sensor = [0,0,0]
    accelData = [0,0,0]
    gyroData = [0,0,0]
    absData = [0,0,0]
    
    while True:
        for j in range(0,len(ad0Pattern)):
            for i in range(0, len(ad0Pattern)):
                for k in range(0,len(ad0Pattern)):
                    ad0PatternFlip[k] = abs(int(ad0Pattern[k]) - 1)
            
                gpio.setPins(ad0PatternFlip)
                ad0Pattern = mpu.ad0Toggle(ad0Pattern)
                
                #print(ad0PatternFlip)
                result1 = mpu.readAccel(sensor1)
                result2 = mpu.readGyro(sensor1)
                #print("Accel retrurned: {}, gyro returned: {}".format(result1, result2))
                try:
                    #print("Accel in degrees = {}".format(mpu.radToDeg(result2)))
                    accelData[i] = result1
                    gyroData[i] = result2
                    absData[i] = mpu.radToDeg(result2)
                except Exception as e:
                    print(e)
                
            time.sleep(0.1)    
            sensor[j] = accelData, gyroData, absData
        
        #print("sensor value = {}".format(sensor[0]))        
        #graph.plotPoints3d(accelData)
        #graph.animate(accelData)
        
if __name__ == "__main__":
    main()

