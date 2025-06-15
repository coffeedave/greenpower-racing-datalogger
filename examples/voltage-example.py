import time
import board
import busio
import adafruit_ina260

i2c = busio.I2C(board.SCL, board.SDA)
ina260 = adafruit_ina260.INA260(i2c)

while True:
    print(
        f"Current: {ina260.current:.2f} mA Voltage: {ina260.voltage:.2f} V Power:{ina260.power:.2f} mW"  # noqa: E501
    )
    time.sleep(1)