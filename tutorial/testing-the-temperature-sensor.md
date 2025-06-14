# Testing the Temperature Sensor

For temperature measurement we are using a digital temperature sensor that is waterproof and able to be used in a harsh environment. Inside the casing is a DS18B20 tempareture module. This can be connected to the Raspberry Pi using one-pin IO.

The DS18B20 uses a 1-Wire communication protocol, which is a single-wire interface. To establish a "high" signal on the data line, a 4.7K pull-up resistor is needed. When the sensor is not actively transmitting data it doesn't actively drive the line high or low. The pull-up resistor ensures the line is pulled high, providing a defined voltage level for the microcontroller to read. 

For testing we will put the resistor on the breadboard, but in the final in-car version it sould make sense to solder it into the circuit.

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

![image](./images/temperature_circuit_image.svg)


