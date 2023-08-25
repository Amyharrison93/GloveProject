'''
library of operation dedicated to translating sensor information into usable information
'''

def calcoffset(sensor1, sensor2):
    '''returns the angle difference between two IMU readings
    return is a tuple of [x,y,z]'''
    sensorOffset = [0,0,0]
    for i in range(0,len(sensor1)):
        sensorOffset[i] = sensor1[i] - sensor2[i]
    
    return sensorOffset