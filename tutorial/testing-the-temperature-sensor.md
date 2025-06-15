# Testing the Temperature Sensor

For temperature measurement we are using a digital temperature sensor that is waterproof and able to be used in a harsh environment. Inside the casing is a DS18B20 tempareture module. This can be connected to the Raspberry Pi using one-pin IO.

The DS18B20 uses a 1-Wire binary communication protocol, which is a single-wire interface. To establish a "high" signal on the data line, a 4.7K pull-up resistor is needed. When the sensor is not actively transmitting data it doesn't actively drive the line high or low. The pull-up resistor ensures the line is pulled high, providing a defined voltage level for the microcontroller to read. 

![image](../images/pullup-resistor-diagram.svg)

For testing we will put the resistor on the breadboard, but in the final in-car version it would make sense to solder it into the circuit.

Note: This section is loosely based on the tutorial [here](https://randomnerdtutorials.com/raspberry-pi-ds18b20-python/) which has more detail on some steps if needed.

# Connecting the Temperature Sensor

To connect the components in the circuit, use a breadboard and follow these steps:

Power Connections:
- Connect the 3.3V pin of the Raspberry Pi Zero 2 W to pin1 of the Resistor.
- Connect pin2 of the Resistor to the Power pin of the DS18B20 Digital Temperature Sensor.
Ground Connections:
- Connect the Ground pin of the Raspberry Pi Zero 2 W to the Ground pin of the DS18B20 Digital Temperature Sensor.
Data Connection:
- Connect the Data pin of the DS18B20 Digital Temperature Sensor to GPIO 4 of the Raspberry Pi Zero 2 W.
- Connect the Data pin of the DS18B20 Digital Temperature Sensor to to pin2 of the Resistor.

**Note:** The colours of the wires on your sensor might not match the diagram below, but usually red is power, white or black is ground, and the remaining colour is the data wire.

![image](../images/temperature_circuit_image.svg)

# Setting up the Pi to Read Temperature

First we need to enable the one-wire interface.

1. Open a Terminal window on your Raspberry Pi (for example, via SSH), type the following command and press Enter.
```
sudo raspi-config
```
2. Go into Menu 3, Interface Options
3. Go down to One-Wire Interface and enable it
4. Exit the config app
5. Restart the Pi

Next, we need to enable the drivers for recording temperature via One-Wire

1. Load the kernel drivers for measuring temperate
```
sudo modprobe w1-gpio
sudo modprobe w1-therm
```
2. Switch to the devices directory
```
/sys/bus/w1/devices/
```
3. List the contents of the devices folder that should show one or more directories, each representing a one-wire device.
```
ls
```
4. If your temperature sensor is connected up correctly then you should see an entry starting "28-". This is the address of your temperature sensor using the One-Wire protocol. If you do not see an entry then you need to check your circuit is correct and ensure one-wire is enabled above.
![image](https://github.com/user-attachments/assets/14779243-0c3b-4aaf-8d76-2af4bc38b33a)

5. switch directories to the directory for your device (change the folder name below based on your device)
```
cd 28-0e24618ad8a6
```
6. In this folder all the one wire data appears as files. Run the following command to output the temperature from the temperature file, this will give you the current temperature. You will need to divide the number by 1000 to get the temperature in deg C.
```
cat temperature
```
![image](https://github.com/user-attachments/assets/fc70dad2-5d14-4a51-a4c2-ed8423c45916)

7. Check it is working by holding the temperature sensor to warm it up and running the command again. You should see the number change.

Your temperature sensor is now setup and working, so now we can try using it from python.

# Reading the temperature from a Python program

A sample python program to read the temperature and output it to the console every second is present in the examples folder.

1. Go to the examples folder
```
cd ~
cd greenpower-racing-datalogger/examples
```
2. Run the sample program
```
python ./read-temperature-example.py
```
This example should output the temperature once every second to the command line.


## Things to Try

- Put the sensor in a glass fo cold water, can you see the temperature change?
- Can you update the python program to write the time and temperature out to a file once a second? This is the first step in turning the sensor into a data-logger

# Sensors for Everything!

One of the great things about the temperature sensors and One-wire is that you can easily have lots of them all connected up to the same pin (the practical limit is about 30 sensors, which is more than enough!). So one easy way to extend the logger is to add more temperature sensors. Each will get a different address and folder in the file system, so you'll need to modify the python code to read from each of them individually.

The circuit update for three sensors would look like this:

![image](../images/temperature_circuit_three_sensors_image.svg)
