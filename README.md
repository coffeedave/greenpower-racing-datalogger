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

# Installation and Connection of the Screen Module


