# Greenpower Racing Datalogger
This is a project to create a Raspberry Pi Zero 2 based data logger for Greenpower Electric Car Racing.

Greenpower run an electric car racing series for schools, [GreenPower Formula 24](https://www.greenpower.co.uk/), where they can build and race an electric car from scratch or from a kit. As part of the racing series it's useful to be able to collect data on the car and driver performance, including speed, track position, component temeratures inside the car, power usage etc. With this information the car performance can be optimised and improved, and drivers coached to improve lap times and race distance.

There are no inexpensive, commercially available, off the shelf tools to record what is needed, and Greenpower is all about learning STEM so we should build one!

This project is designed to be a tutorial and guide to create a data logger from scratch using common raspberry pi based components that the team can build and utilise for race performance.

## Design Principles
This data logger is intended to be able to be constructed by a School team (Year 7+) on thier own out of commonly available parts. Electronics, soldering, Linux command line, Python programming, 3D CAD, 3D printing and other skills are needed to be able to complete and test the logger. To install it in the car the team will need to create cases for all the components as well as work out how to run a wiring loom to bring all the sensor data back to the location of the RPi.

In general the design principles are:
- Common off the shelf, easily replacable components (Someone is going to break them as some point!)
- No custom PCB boards or integrated circuits
- Able to be assembled and tested in sections on breadboards to get familiar with each component
- Provide a reliable, tested way to assemble the data logger to minimise frustration and troubleshooting
- Uses tools and technology a secondary school DT and computing departments are likey to already have access to (3d Printers, Raspberry Pi's etc.)
- Focus on low cost wherever possible
- Provide working python code samples for each component to simplify testing
- Provide sample files for any 3D printed parts that can be customised

# High Level Design Overview

The goal is to get a set of data about the car with timestamps that can be analysed by the team after each race or practice session. For the the initial version of the datalogger the following sensors are to be used:

- GPS Sensor for location, speed and for accurate clock timing
- Current / Voltage Sensor to measure battery usage and motor power
- Temperature sensor to measure the motor temperature and understand if it is overheating

Each of these sesnors is connected to a Raspberry Pi which reads from them frequently and writes the details from each to a file.

There is also an optional screen, which can be used to show the driver live information on car performance, or to help understand if the RPi is up and running correctly.

After the race, the file containing the race data can be copied to another computer and then analysed using any tools the team have at thier disposal such as Excel, charting software etc.

## Taking it Further
Once the basic data logger is built there are lots of ways to extend the project, and the direction is up to the members of the racing team, but some ideas are:

- Add additional sensors for other areas of the car
- Be able to connect remotely to the data logger to get data quickly after a race
- Make the data logger upload to a second Rpi server so you can view Real-Time race information
- Add 3G/4G mobile data to the logger so it is contactable on the far side of the track
- Use the RPi as a controller for other aspects of the car
- Get the data logger to output in formats that can be read by professional racing software such as [VBOX Circuit Tools](https://www.vboxmotorsport.co.uk/index.php/en/circuit-tools) (which is free to use)

## Repository Struture

This git repository is structured as follows:

- tutorial - tutorials for building and creating the data logger and testing each component
- examples - contains pythin code samples used in the tutorial
- examples/lib - contains libray files needed by python to drive some of the components

# Hardware Needed
All hardware can be obtained easily from thepihut or Amazon. Total cost is around £85 (2025 prices). Cost can be reduced by leaving out optional components, or reducing the number of sensors used.

| Hardware                    | Image | Description | Required | Link |
| --------------------------- | ----- | ----------- | -------- | ---- | 
| Raspberry Pi Zero 2 W | ![image](https://github.com/user-attachments/assets/908d660e-8008-4785-9e97-460538e46870) | Microcomputer chosen as it runs on very little power cand can be easily programmed. If possible get the "WH" model as it already has the header pins soldered on saving some work | Yes | [Link](https://www.raspberrypi.com/products/raspberry-pi-zero-2-w/) |
| Adafruit Ultimate GPS Breakout - 66 channel w/10 Hz updates (Version 3) | ![image](https://github.com/user-attachments/assets/1559135c-964e-4596-9e3b-0be03b289cbe) | GPS Sensor with 1/10 second capture frequency | Yes | [Link](https://thepihut.com/products/adafruit-ultimate-gps-breakout-66-channel-w-10-hz-updates) |
| Freenove LCD2004 | ![image](https://github.com/user-attachments/assets/be971ebc-6eaf-4d04-9de1-8cf559d1bc2c) |  LCD2004 screen module with PCF8574 I2C controller. There are Adafruit and generic versions of this. | Yes | [Link](https://store.freenove.com/products/fnk0079?variant=43034492797126) |
| Waterproof DS18B20-Compatible Temperature Sensor with Resistor | ![image](https://github.com/user-attachments/assets/62dd4732-b075-497d-a42a-422fcae3ddc0) | Temperature sensor that can be used in a harsh environment for measuring motor temperature etc. | Yes | [Link](https://thepihut.com/products/waterproof-ds18b20-digital-temperature-sensor-extras)
| Adafruit INA260 High or Low Side Voltage, Current, Power Sensor | ![image](https://github.com/user-attachments/assets/5e23132f-f37f-425d-99cd-e305cbca2c8a)  | Current and Voltage Sensor for measuring power | Yes| [Link](https://thepihut.com/products/adafruit-ina260-high-or-low-side-voltage-current-power-sensor-ada4226) |
| GPS Antenna - External Active Antenna - 3-5V 28dB 5 Meter SMA | ![image](https://github.com/user-attachments/assets/c5b3984f-ceab-4372-8106-e0a4daca634d)  |  External antenna for the GPS module to improve reception and increase precision for GPS readings. This is not needed as the GPS modulae has an inbuilt antenna, but it allows the GPS module to be hidden away in the final version. | Optional | [Link](https://thepihut.com/products/gps-antenna-external-active-antenna-3-5v-28db-5-meter-sma) |
| SMA to uFL/u.FL/IPX/IPEX RF Adapter Cable | ![image](https://github.com/user-attachments/assets/ff412d27-0ad2-417f-94b4-1099345a3e3a) | Used with the GPS antenna to be able to connect it to the GPS Breakout Board | Optional | [Link](https://thepihut.com/products/sma-to-ufl-u-fl-ipx-ipex-rf-adapter-cable) |
| Various wires and connectors  | ![image](https://github.com/user-attachments/assets/ac88306e-6e33-4644-8d53-343280e82ea3) | To link things together. May also need some RJ45 connectors and sockets or similar for mounting the wiring loom in the car and being able to disconnect it | Yes | |
| 3d Printer | ![image](https://github.com/user-attachments/assets/221870c9-a763-4c1f-89e6-4b96e48019c0) | So the team can design, build, and print some awesome cases to hold all the components and mount them in the vehicle. It's got to look insane — No Cap. | Of course! 3d printers rock! |  |


# Setting up the raspberry Pi

## Initial Setup

The raspberry pi should have the latest RasberryPi OS running on it, setup as per the instructions on the Rasberry Pi Website. Use the raspberry Pi imager to get the pi setup with wifi networking and ssh (so we can connect to it remotely).

Ensure the rasberry pi is fullly up to date by running the following at a command line:

```
sudo apt-get update
sudo-apt-get upgrade
```

Check and verify that it is possible to connect to the RPi remotely from another computer using ssh (linux) or [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty) (Windows). There are plenty of tutorials out there to assist with this step, but if you can log into the Pi Remotely using these tools, then we're good to start the next step!

To get all the sample code and files onto the raspberry pi you can clone this github repository to the home folder.

```
cd ~
git clone https://github.com/coffeedave/greenpower-racing-datalogger.git
```

This will create a copy of all the files here in a folder called greenpower-racing-datalogger

If you need to update the files to the latest version you can use the following command (**Note:**
 this will potentially overwrite any modifications to code made by students)

```
cd ~
cd greenpower-racing-datalogger
git pull
```

## Building the Data Logger

To create the data logger, it makes sense to test each component individually with the RPi, get it working, and be able to write some code to control it. That way you get familiar with how each component works, understand how to connect it up, and ensure that the RPi can use each successfully. One all components are working, we can then connect everything up and write some code to link them all together into the full scale data logger!

We are going to be using Python as the programming language for each module, so it will be easy to combine the code for each component together at the end.

Each of the next sections takes you through building and testing a system with each component. Make sure each is working before you move on as some rely on you completing the earlier sections.

1. [Testing the Screen Module](./tutorial/testing-the-screen-module.md)
2. [Testing the Temperature Sensor](./tutorial/testing-the-temperature-sensor.md)
3. [Testing the Current and Voltage Module](./tutorial/testing-the-voltage-sensor.md)
4. [Testing the GPS Module](./tutorial/testing-the-gps-module.md)
5. Connecting everything together
7. Coding the data logger
8. Installation in the car
