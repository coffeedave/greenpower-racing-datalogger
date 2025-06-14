# Import the required system libraries
import os
import glob
import time

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
while True:
    # Print the value of the temperature from the sensor
	print('Temperature: ' + read_temp())	
      
    # Wait for one Second
	time.sleep(1)
