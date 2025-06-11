# ghs-racing-datalogger
Project to Create and document creation of a Raspberri Pi Zero 2 based data logger for Greenpower Electric Car Racing

GHS have an electric car racing team that competes in the GreenPower Formula 24 racing series (https://www.greenpower.co.uk/). As part of the racing series it's useful to be able to collect data on the car and driver performance, including speed, track position, component temeratures inside the car, power usage etc. With this information the car performance can be optimised and improved, and drivers coached to improve lap times and race distance.

There are no commercially avaialble off the shelf tools to record what is needed, and as a result this project is designed to be a tutorial and guide to create a data logger from scratch using common raspberry pi based components that the team can build and utilise for race performance.

# High Level Design Overview


# Hardware Needed
All hardware can be obtained easily from thepihut or Amazon. Total cost is around £85 (2025 prices)

- Raspberry Pi Zero 2 W
- Adafruit INA260 Breakout Voltage and Current Sensor
- Adafruit GPS Breakout
- LCD2004 screen module with PCF8574 I2C controller (for example freenove LCD2004, which combines both into a single package)
- Optional: GPS Antenna and connecting cable
- Various wires and connectors to link things together
- 

# Setting up the raspberry Pi

## Initial Setup

The raspberry pi should have the latest RasberryPi OS running on it, setup as per the instructions on the Rasberry Pi Website. Use the raspberry Pi imager to get the pi setup with wifi networking and ssh (so we can connect to it remotely).

Check and verify that it is possible to connect to the RPi using ssh (linux) or PuTTY (windows). There are plenty of tutorials out there to assist with this step, but if you can log into the Pi Remotely using these tools, then we're good to start the next step!

## Building the Data Logger

To create the data logger, it makes sense to test each component individually with the RPi, get it working, and be able to write some code to control it. That way you get familiar with how each component works, understand how to connect it up, and ensure that the RPi can use each successfully. One all components are working, we can then connect everything up and write some code to link them all together into the full scale data logger!

We are going to be using Python as the programming language for each module, so it will be easy to combine the code for each component together at the end.

Each of the next sections can be done in any order, but make sure each is working before you move on.

### Installation and Testing of the Screen Module
The official installation instrcutions for the freenove module that is used in the intial build of the data logger can be found here: https://github.com/Freenove/Freenove_LCD_Module/archive/refs/heads/main.zip

To be able to test the screen we first need to enable the drivers for the screen on the RPi as well as the interface commands it will be using. This screen uses the I2C serial interface on the Pi, so we need to turn it on to be able to use it.

1. Log into the RPi
2. Run the RPi configuration utility
        sudo raspi-config
3. From the Interfaces option, enable the I2C interface
4. Save the settings
5. Restart the RPi
6. Once it has restarted, we can check the I2C interface is running by using
         lsmod | grep i2c
   If the RPi bus is up and running then you should see something like the following

   <Insert Picture Here>

Once it's restarted we then need to install some modules to help us work with the I2C interface

1. Log into the RPi
2. At a command prompt run the following to install I2C-tools
        sudo apt-get install i2c-tools
3. Install the python smbus modules so we can control the device from python 
        sudo apt-get install python-smbus
         sudo apt-get install python3-smbus
   
5. Install I2C Device Detection
           i2c
