'''
address definitions for the MPU6050 sensor
'''
MPU6050_I2CADDR_DEFAULT : int =  0x68    #///< MPU6050 default i2c address w/ AD0 high
MPU6050_DEVICE_ID : int =  0x68    #///< The correct MPU6050_WHO_AM_I value
MPU6050_DEVICE_ID_2 : int =  0x69    #///< The correct MPU6050_WHO_AM_I value
MPU6050_SELF_TEST_X : int =  0x0D    #///< Self test factory calibrated values register
MPU6050_SELF_TEST_Y : int =  0x0E    #///< Self test factory calibrated values register
MPU6050_SELF_TEST_Z : int =  0x0F    #///< Self test factory calibrated values register
MPU6050_SELF_TEST_A : int =  0x10    #///< Self test factory calibrated values register
MPU6050_SMPLRT_DIV : int =  0x19    #///< sample rate divisor register
MPU6050_CONFIG : int =  0x1A    #///< General configuration register
MPU6050_GYRO_CONFIG : int =  0x1B    #///< Gyro specfic configuration register
MPU6050_ACCEL_CONFIG : int =  0x1C    #///< Accelerometer specific configration register
MPU6050_INT_PIN_CONFIG : int =  0x37    #///< Interrupt pin configuration register
MPU6050_INT_ENABLE : int =  0x38    #///< Interrupt enable configuration register
MPU6050_INT_STATUS : int =  0x3A    #///< Interrupt status register
MPU6050_SIGNAL_PATH_RESET : int =  0x68    #///< Signal path reset register
MPU6050_USER_CTRL : int =  0x6A    #///< FIFO and I2C Master control register
MPU6050_PWR_MGMT_1 : int =  0x6B    #///< Primary power/sleep control register
MPU6050_PWR_MGMT_2 : int =  0x6C    #///< Secondary power/sleep control register
MPU6050_TEMP_H : int =  0x41    #///< Temperature data high byte register
MPU6050_TEMP_L : int =  0x42    #///< Temperature data loegister
MPU6050_WHO_AM_I : int =  0x75    #///< Divice ID register
MPU6050_SIGNAL_PATH_RESET : int =  0x68    #///< Signal path reset register
MPU6050_USER_CTRL : int =  0x6A    #///< FIFO and I2C Master control register
MPU6050_PWR_MGMT_1 : int =  0x6B    #///< Primary power/sleep control register
MPU6050_PWR_MGMT_2 : int =  0x6C    #///< Secondary power/sleep control register
MPU6050_TEMP_H : int =  0x41    #///< Temperature data high byte register
MPU6050_TEMP_L : int =  0x42    #///< Temperature data low byte register
MPU6050_ACCEL_OUT : int =  0x3B    #///< base address for sensor data reads
MPU6050_MOT_THR : int =  0x1F    #///< Motion detection threshold bits [7:0]
MPU6050_MOT_DUR : int =  0x20    #///< Duration counter threshold for motion int. 1 kHz rate, LSB = 1 ms

#Accelerometer range select 
MPU6050_RANGE_2_G : int =  0b00   #///< +/- 2g 
MPU6050_RANGE_4_G : int =  0b01   #///< +/- 4g
MPU6050_RANGE_8_G : int =  0b10   #///< +/- 8g
MPU6050_RANGE_16_G : int =  0b11   #///< +/- 16g