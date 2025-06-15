from gps import *
import time

#Import the screen libraries in case we want to write to the screen
from PCF8574 import PCF8574_GPIO
from Adafruit_LCD2004 import Adafruit_CharLCD

def getPositionData(gps):
    nx = gpsd.next()
    # For a list of all supported classes and fields refer to:
    # https://gpsd.gitlab.io/gpsd/gpsd_json.html
    if nx['class'] == 'TPV':
        latitude = getattr(nx,'lat', "Unknown")
        longitude = getattr(nx,'lon', "Unknown")
        print("Your position: lon = " + str(longitude) + ", lat = " + str(latitude))
        print("Speed (km/h): " + str(getattr(nx,'speed', "0") * 3.6))
    return getattr(nx,'speed', "0") * 3.6

gpsd = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE)


PCF8574_address = 0x27  # I2C address of the PCF8574 chip.
PCF8574A_address = 0x3F  # I2C address of the PCF8574A chip.
# Create PCF8574 GPIO adapter.
try:
    mcp = PCF8574_GPIO(PCF8574_address)
except:
    try:
        mcp = PCF8574_GPIO(PCF8574A_address)
    except:
        print ('I2C Address Error !')
        exit(1)
# Create LCD, passing in MCP GPIO adapter.
lcd = Adafruit_CharLCD(pin_rs=0, pin_e=2, pins_db=[4,5,6,7], GPIO=mcp)

mcp.output(3,1)     # turn on LCD backlight
lcd.begin(20,4)     # set number of LCD lines and columns
lcd.setCursor(0,0)  # set cursor position
lcd.message( 'Greenpower')

try:
    print("Application started!")
    while True:
        getPositionData(gpsd)
        lcd.message( 'Speed: ' + f"{getPositionData(gpsd):.1f}" +'\n' )# display Current Speed
        time.sleep(1.0)

except (KeyboardInterrupt):
    running = False
    print("Applications closed!")