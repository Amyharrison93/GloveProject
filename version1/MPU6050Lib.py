'''
library containing funtions to make the MPU6050 easier to work with
'''

from math import degrees, atan2, pi
from os import getcwd
from sys import path
from board import I2C
from adafruit_mpu6050 import MPU6050
from numpy import zeros

path.append(getcwd())
import MPU6050Def as mpuDef

def vector_2_degrees(x, y):
    angle = degrees(atan2(y, x))
    if angle < 0:
        angle += 360
    return angle

def ad0Init(patternLength : int):
    '''initialises the pattern required for activating the correct ad0
    patternLength is an integer corrosponding to the number of MPU6050 sensors being used'''
    
    ad0Pattern = zeros(patternLength, int)
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
        i2c = I2C()  # uses board.SCL and board.SDA
        mpu = MPU6050(i2c, intAddr)
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
    
def getAccelAngle(mpu):
    '''gets the vector angle of the IMU from the accelerometer data
    returns tuple of floats'''
    x, y, z = mpu.acceleration
    return vector_2_degrees(x, z), vector_2_degrees(y, z), vector_2_degrees(x, y)

def radToDeg(rad):
    '''converts an array of radians into degrees
    returns an array the same size as the input containing floats'''
    deg = zeros(len(rad))
    for i in range(0, len(rad)):
        deg[i] = (float(rad[i]) * 180)/pi
    return deg

def rVector(accel):
    '''caLculated the r vector of the accelerometer
    returns float rvector'''
    rVector = (accel[0]^2)+(accel[1]^2)+(accel[2]^2) 
    return rVector
    
def gyroAngle(gyro, deltaTime, arryOrientation = [0,0,0]):
    '''calculates the absolute orientation from the acceleration and the gyroscope data
    returns an array[3] of X, Y and Z rotations 
    this does not work'''
    gyroDeg = radToDeg(gyro)
    gyroDeg = gyro
    
    arryOrientation = (
        (arryOrientation[1] + gyroDeg[1]) * deltaTime,     #pitch x
        (arryOrientation[0] + gyroDeg[0]) * deltaTime,     #yaw y
        (arryOrientation[2] + gyroDeg[2]) * deltaTime,     #roll z
    )
    
    return arryOrientation

def readTemp(mpu):
    '''read current sensor temperiture
    returns float temperiture value in celcius'''
    try:
        temp = mpu.temperature

        return temp
    
    except Exception as e:
        return e