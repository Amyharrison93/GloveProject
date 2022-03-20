#!/usr/bin/env python

import os
import sys
import time
from datetime import datetime
from numpy import zeros
sys.path.append(os.getcwd())

import MPU6050Lib as mpu
import rpiGPIOLib as gpio
import GloveOperations as glvOp
#import GraphOutLib as graph

def main():
    '''
    Main program function
    '''
    
    nowTime = datetime.now()
    
    sensorCount : int = 4
    sensorMain : int = 0
    
    sensor = [0,0,0]
    accelData = [0,0,0]
    gyroData = [0,0,0]
    accelAngleData = [0,0,0]
    gyroAngleData = [0,0,0]
    gyroAngleData = [0,0,0]
    
    output = zeros(sensorCount)
    
    #graph.TestPlot()
    gpio.gpioSetup(sensorCount)
    gpio.pinInit()
    
    ad0Pattern = mpu.ad0Init(sensorCount)
    ad0PatternFlip = mpu.ad0Init(sensorCount)
    
    for i in range(0, len(ad0PatternFlip)):
        ad0PatternFlip[i] = abs(int(ad0PatternFlip[i]) - 1)
    gpio.setPins(ad0PatternFlip)
    
    time.sleep(0.1)
    
    imu1 = mpu.initSensor(0x68)
    
    time.sleep(0.1)
    
    while True:
        for j in range(0,len(ad0Pattern)):
            for i in range(0, len(ad0Pattern)):
                for k in range(0,len(ad0Pattern)):
                    ad0PatternFlip[k] = abs(int(ad0Pattern[k]) - 1)
            
                gpio.setPins(ad0PatternFlip)
                ad0Pattern = mpu.ad0Toggle(ad0Pattern)
                
                #print(ad0PatternFlip)
                prvTime = nowTime
                nowTime = datetime.now()
                deltaTime = nowTime - prvTime
                deltaTime = deltaTime.total_seconds()
                
                accelRead = mpu.readAccel(imu1)
                gyroRead = mpu.readGyro(imu1)
                accelAngle = mpu.getAccelAngle(imu1)
                
                try:
                    accelData[i] = accelRead
                    gyroData[i] = gyroRead
                    accelAngleData[i] = accelAngle
                    
                    try:
                        gyroAngleData[i] = mpu.radToDeg(mpu.gyroAngle(gyroRead, deltaTime, gyroAngleData[i]))
                    except: 
                        gyroAngleData[i] = mpu.gyroAngle(gyroRead, deltaTime)
                    #print("sensor 1 abs roll = : {}, gyro data = {}, timeDelta = {}".format(gyroAngleData[1][0], gyroData[1][0], deltaTime))
                    
                except Exception as e:
                    print(e)
                
                time.sleep(0.01)    
            sensor[j] = accelData, gyroData, gyroAngleData
            
            #for i in sensor:
            #    if i == 1:
            #        for j in sensor[sensorMain]:
            #            output[i][j] = sensor[sensorMain][j]
            #    else: 
            #        output[i] = glvOp.calcoffset(sensor[sensorMain], sensor[i])
            #print(output)
        
        #print("sensor value = {}".format(sensor[0]))        
        #graph.plotPoints3d(accelData)
        #graph.animate(accelData)
        
if __name__ == "__main__":
    main()

