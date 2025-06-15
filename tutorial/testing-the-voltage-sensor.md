# Testing the Voltage and Current Sensor

For voltage and current measurement we are using an Adafruit INA260 High or Low Side Voltage, Current and Power Sensor.

This communicates with the Pi using serial logic, and allows use to read information via the Pi's Serial pins.

# Connecting the Voltage and Current Sensor

The pinout Diagram for the sensor is below.

![image](https://github.com/user-attachments/assets/5702cac1-4be6-48b4-a95f-c175bfd7bb4c)


# Setting up the Pi to Read Voltage and Current


# Reading Voltage and Current from a Python program

1. Install required libraries for i2c and virtual environenments
```
cd ~
sudo apt-get install -y i2c-tools libgpiod-dev python3-libgpiod
sudo apt install python3-venv
```

2. Create a virtual environment
```
python3 -m venv env --system-site-packages
```

3. activate python virtual environment
```
source env/bin/activate
```

4. Now install the Adafuit Blinka Library
```
pip3 install --upgrade adafruit-blinka
```

## Things to Try

