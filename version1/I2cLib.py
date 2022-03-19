from smbus2 import SMBus as smb

def testRead(addr: int, intChannel: int = 1):
    '''Test read function for I2C bus
    address as int 0xXX format
    intChannel defaults to 1'''
    try:
        bus = smb(intChannel)
        bus.write_byte(addr, 0b110100000)
        i2cRead = bus.read_i2c_block_data(0b1101000, 0, 32)
        print("17 byte i2c read = {}".format(i2cRead))
    except Exception as e:
        print(e)

def testWrite(message, addr: int, intChannel: int = 1):
    '''Test write function for I2C bus
    message as 
    address as int 0xXX format
    intChannel defaults to 1'''
    try:
        bus = smb(intChannel)
        i2cRead = bus.read_byte(addr)
        print(bus.write_byte(addr, 0x01))
    except Exception as e:
        print(e)