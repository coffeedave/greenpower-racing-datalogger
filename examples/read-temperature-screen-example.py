# Import the required system libraries
import os
import glob
import time

#Import the screen libraries in case we want to write to the screen
from PCF8574 import PCF8574_GPIO
from Adafruit_LCD2004 import Adafruit_CharLCD

# Enable the operating system drivers for one-wire temperature devices
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

# Get the address details of the temperature sensor from the file system
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0] #This locates the first device that starts with "28" in the folder
device_file = device_folder + '/temperature'

# Function to read the temperature sensor information from the device
def read_temp():
    # Open the one-wire device file on the file system that contains the temperature
    f = open(device_file, 'r')

    # Read the value of the temperature from the file as a string
    temp_string = f.readlines()[0]

    # Convert the string value into the temperature in deg C as a number
    temp_c = float(temp_string) / 1000.0

    # Close the device file as we have finished reading from it
    f.close()

    # Return the Temperature to the calling program
    return temp_c

# Main body of the program

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

while True:  
      
    # Put the latest Temperature on the Screen
    lcd.setCursor(0,2)  # set cursor position
    lcd.message( 'Temp: ' + str(read_temp()).format("{a:.1f}")+'\n' )# display Sensor temperature formatted to one decimal place  

    # Wait for one Second
    time.sleep(1)
