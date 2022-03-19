from math import degrees
import os
import sys
import board
import adafruit_mpu6050
import numpy as np

sys.path.append(os.getcwd())
import MPU6050Def as mpuDef

def ad0Init(patternLength : int):
    '''initialises the pattern required for activating the correct ad0
    patternLength is an integer corrosponding to the number of MPU6050 sensors being used'''
    
    ad0Pattern = np.zeros(patternLength, int)
    ad0Pattern[0] = 1
    
    return ad0Pattern

def ad0Toggle(ad0Pattern):
    '''toggles the bit related to the sensor being read at any given time
    ad0Pattern is an array with a length related to the number of sensors being used'''
    ad0Increment = False
    if ad0Pattern[len(ad0Pattern) - 1] != 1:
        for i in range(0, len(ad0Pattern)):
            if ad0Pattern[i] == 1 and not ad0Increment:
                ad0Pattern[i] = 0
                ad0Pattern[i+1] = 1
                ad0Increment = True
            if ad0Increment and ad0Pattern[i] == 1:
                ad0Increment = False
                                
    else:
        ad0Pattern = ad0Init(len(ad0Pattern))
    
    return ad0Pattern

def initSensor(intAddr : int = mpuDef.MPU6050_DEVICE_ID):
    '''initialise the MPU6050 sensor 
    default address 0x68'''
    try:
        i2c = board.I2C()  # uses board.SCL and board.SDA
        mpu = adafruit_mpu6050.MPU6050(i2c, intAddr)
        return mpu
    
    except Exception as e:
        return e

def readGyro(mpu, intAddr : int = mpuDef.MPU6050_DEVICE_ID):
    '''read current gyroscope values
    returns array of 3 floats for X, Y and Z '''
    try:
        arryGyro = mpu.gyro

        return arryGyro
    
    except Exception as e:
        return e

def readAccel(mpu, intAddr : int = mpuDef.MPU6050_DEVICE_ID):
    '''read current accelerometer values
    returns array of 3 floats for X, Y and Z '''
    try:
        arryAccel = mpu.acceleration
        return arryAccel
    
    except Exception as e:
        return e
    
def radToDeg(rad):
    '''converts an array of radians into degrees
    returns an array the same size as the input containing floats'''
    print(rad)
    deg = np.zeros(len(rad))
    for i in range(0, len(rad)):
        deg[i] = (float(abs(rad[i])) * 57.295779513)%360
    return deg
    
def absOrientation(accel, gyro):
    '''calculates the absolute orientation from the acceleration and the gyroscope data
    returns an array[3] of X, Y and Z rotations '''
    arryOrientation = [0,0,0]
    
    
    return arryOrientation

def readTemp(mpu, intAddr : int = mpuDef.MPU6050_DEVICE_ID):
    '''read current sensor temperiture
    returns float temperiture value in celcius'''
    try:
        temp = mpu.temperature

        return temp
    
    except Exception as e:
        return e