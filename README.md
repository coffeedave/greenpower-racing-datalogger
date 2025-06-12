# ghs-racing-datalogger
Project to Create and document creation of a Raspberri Pi Zero 2 based data logger for Greenpower Electric Car Racing

GHS have an electric car racing team that competes in the GreenPower Formula 24 racing series (https://www.greenpower.co.uk/). As part of the racing series it's useful to be able to collect data on the car and driver performance, including speed, track position, component temeratures inside the car, power usage etc. With this information the car performance can be optimised and improved, and drivers coached to improve lap times and race distance.

There are no commercially avaialble off the shelf tools to record what is needed, and as a result this project is designed to be a tutorial and guide to create a data logger from scratch using common raspberry pi based components that the team can build and utilise for race performance.

# High Level Design Overview


# Hardware Needed
All hardware can be obtained easily from thepihut or Amazon. Total cost is around £85 (2025 prices). Cost can be reduced by leaving out optional components, or reducing the number of sensors used.

| Hardware                  | Image | Description | Required | Link |
| --------------------------- | --- | --- | ---- | --- | --- |
| Raspberry Pi Zero 2 W | ![image](https://github.com/user-attachments/assets/908d660e-8008-4785-9e97-460538e46870) | Microcomputer chosen as it runs on very little power cand can be easily programmed. If possible get the "WH" model as it already has the header pins soldered on saving some work | Yes | [Link](https://www.raspberrypi.com/products/raspberry-pi-zero-2-w/) |
| Adafruit Ultimate GPS Breakout - 66 channel w/10 Hz updates (Version 3) | ![image](https://github.com/user-attachments/assets/1559135c-964e-4596-9e3b-0be03b289cbe) | GPS Sensor with 1/10 second capture frequency | Yes | [Link](https://thepihut.com/products/adafruit-ultimate-gps-breakout-66-channel-w-10-hz-updates) |
| Freenove LCD2004 | ![image](https://github.com/user-attachments/assets/be971ebc-6eaf-4d04-9de1-8cf559d1bc2c) |  LCD2004 screen module with PCF8574 I2C controller. There are Adafruit and generic versions of this. | Yes | [Link](https://store.freenove.com/products/fnk0079?variant=43034492797126) |
| Waterproof DS18B20-Compatible Temperature Sensor with Resistor | ![image](https://github.com/user-attachments/assets/62dd4732-b075-497d-a42a-422fcae3ddc0) | Temperature sensor that can be used in a harsh environment for measuring motor temperature etc. | Yes | [Link](https://thepihut.com/products/waterproof-ds18b20-digital-temperature-sensor-extras)
| Adafruit INA260 High or Low Side Voltage, Current, Power Sensor | ![image](https://github.com/user-attachments/assets/5e23132f-f37f-425d-99cd-e305cbca2c8a)  | Current and Voltage Sensor for measuring power | Yes| [Link](https://thepihut.com/products/adafruit-ina260-high-or-low-side-voltage-current-power-sensor-ada4226) |
| GPS Antenna - External Active Antenna - 3-5V 28dB 5 Meter SMA | ![image](https://github.com/user-attachments/assets/c5b3984f-ceab-4372-8106-e0a4daca634d)  |  External antenna for the GPS module to improve reception and increase precision for GPS readings. This is not needed as the GPS modulae has an inbuilt antenna, but it allows the GPS module to be hidden away in the final version. | Optional | [Link](https://thepihut.com/products/gps-antenna-external-active-antenna-3-5v-28db-5-meter-sma) |
| SMA to uFL/u.FL/IPX/IPEX RF Adapter Cable | ![image](https://github.com/user-attachments/assets/ff412d27-0ad2-417f-94b4-1099345a3e3a) | Used with the GPS antenna to be able to connect it to the GPS Breakout Board | Optional | [Link](https://thepihut.com/products/sma-to-ufl-u-fl-ipx-ipex-rf-adapter-cable) |
| Various wires and connectors  | ![image](https://github.com/user-attachments/assets/ac88306e-6e33-4644-8d53-343280e82ea3)
 | To link things together. May also need some RJ45 connectors and sockets or similar for mounting the wiring loom in the car and being able to disconnect it | Yes | |
| 3d Printer | ![image](https://github.com/user-attachments/assets/221870c9-a763-4c1f-89e6-4b96e48019c0) | So the team can design, build, and print some awesome cases to hold all the components and mount them in the vehicle. It's got to look insane — No Cap. | Obviously |  |


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

```
sudo raspi-config
```

4. From the Interfaces option, enable the I2C interface
5. Save the settings
6. Restart the RPi
7. Once it has restarted, we can check the I2C interface is running by using
```
lsmod | grep i2c
```
8. If the RPi bus is up and running then you should see something like the following

![Screenshot of RPi command output](https://github.com/coffeedave/ghs-racing-datalogger/images/Screenshot 2025-06-11 191118.png)

Once it's restarted we then need to install some modules to help us work with the I2C interface

1. Log into the RPi
2. At a command prompt run the following to install I2C-tools
```
sudo apt-get install i2c-tools
```
4. Install the python smbus modules so we can control the device from python. These provide the connection between python and the underlying hardware.
```
sudo apt-get install python-smbus
sudo apt-get install python3-smbus
```   
5. If you get messages saying these modules are already installed and up to date, then that is fine.

pip3 install Adafruit-Blinka
