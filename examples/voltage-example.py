import time
import board
import busio
import adafruit_ina260

i2c = busio.I2C(board.SCL, board.SDA)
ina260 = adafruit_ina260.INA260(i2c)

print("Current:", ina260.current)
print("Voltage:", ina260.voltage)
print("Power:", ina260.power)