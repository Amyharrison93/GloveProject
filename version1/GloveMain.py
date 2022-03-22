#!/usr/bin/env python

from os import getcwd
from sys import path
from datetime import datetime
from numpy import zeros
from time import sleep
path.append(getcwd())

import MPU6050Lib as mpu
import rpiGPIOLib as gpio
import GloveOperations as glvOp
import DataOutLib as data
#import GraphOutLib as graph

def main():
    '''
    Main program function
    '''
    
    fileName = "GloveDataCapture"
    data.writeCSV(fileName,"")
    nowTime = datetime.now()
    nowTime2 = datetime.now()
    
    sensorCount : int = 7
    sensorMain : int = 0
    count : int = 0
    
    sensor = zeros(shape = (sensorCount, 3))
    accelData = zeros(shape = (sensorCount, 3))
    gyroData = zeros(shape = (sensorCount, 3))
    accelAngleData = zeros(shape = (sensorCount, 3))
    gyroAngleData = zeros(shape = (sensorCount, 3))
    gyroAngleData = zeros(shape = (sensorCount, 3))
    output = zeros(shape = (sensorCount, 3))
    
    #graph.TestPlot()
    gpio.gpioSetup(sensorCount)
    gpio.pinInit()
    
    ad0Pattern = mpu.ad0Init(sensorCount)
    ad0PatternFlip = mpu.ad0Init(sensorCount)
    
    for i in range(0, len(ad0PatternFlip)):
        ad0PatternFlip[i] = abs(int(ad0PatternFlip[i])-1)
        
    gpio.setPins(ad0PatternFlip)
    
    sleep(0.1)
    
    imu1 = mpu.initSensor(0x68)
    
    sleep(0.1)
    
    while True:
        data.appendCSV(fileName, "{},".format(str(datetime.now())))
        
        prvTime = nowTime
        nowTime = datetime.now()
        deltaTime = nowTime - prvTime
        deltaTime = deltaTime.seconds
        #print(deltaTime)
        
        data.appendCSV(fileName, "{}". format(str(deltaTime)))

        for j in range(0,len(ad0Pattern)):
            for i in range(0, len(ad0Pattern)):
                prvTime2 = nowTime2
                nowTime2 = datetime.now()
                deltaTime2 = nowTime2 - prvTime2
                deltaTime2 = deltaTime2.seconds
                #print(deltaTime2)
                
                ad0Pattern = mpu.ad0Toggle(ad0Pattern)
                
                
                for k in range(0,len(ad0Pattern)):
                    ad0PatternFlip[k] = abs(int(ad0Pattern[k]) - 1)
                
                gpio.setPins(ad0PatternFlip)
                
                #print(ad0PatternFlip)
                
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
                    #print("sensor {} abs roll = : {}, gyro data = {}, timeDelta = {}".format(i, accelAngleData[i][0], gyroData[i][0], deltaTime))
                    
                except Exception as e:
                    print(e)
                
                #sleep(0.01)
            
                for k in range(0, len(sensor)):
                        #output[k] = glvOp.calcoffset(accelAngleData[sensorMain], accelAngleData[k])
                        output[k] = accelAngleData[k]
                        if count < 500:
                            data.appendCSV(fileName, "{},".format(str(output[k]).replace(" ", ",").replace("[", "").replace("]","")))
            #print(output)
            if count < 501:
                count += 1
            elif count == 501:
                print("===============================Finished data collection=======================================")
                count += 1
        data.appendCSV(fileName, "\r\n,")
        #print("sensor value = {}".format(sensor[0]))        
        #graph.plotPoints3d(accelData)
        #graph.animate(accelData)
        
if __name__ == "__main__":
    main()

