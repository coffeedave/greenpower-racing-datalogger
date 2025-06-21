# Testing the GPS Module

The GPS module uses sattelites to track the location of the raspberry pi. When it is powered on it will look for sattelites to lock onto, locate itself and then start sending updates to the raspberry Pi.

The module has a built in aerial, but it needs ot be able to see the sky to work, so it will not be able to get a lock if used indoors. Luckily it's possible to add an external aerial to the module which can be located outside, allowing the 

# Circuit

To use the module with the Pi we need to connect them together. The GPS module uses serial transmit and recieve (RX/TX) which the RPi has ports for. To connect it up you need to make the following connections:

To connect the Adafruit Ultimate GPS v3 and the Raspberry Pi Zero 2 W, you can follow these common connections:

Power Connections:
- Connect the VIN pin of the GPS to a suitable power source (e.g., 3.3v from the Raspberry Pi).
- Connect the GND pin of the GPS to a Ground pin on the Raspberry Pi.

Serial Communication:
- Connect the TX pin of the GPS to GPIO 15 (UART RX) on the Raspberry Pi for receiving data.
- Connect the RX pin of the GPS to GPIO 14 (UART TX) on the Raspberry Pi for sending data.

Other Connections:
- Connect the FIX pin to GPIO 23 so we can  monitor the GPS fix status.

A diagram of the circuit is below:
![image](../images/gps_circuit_image.svg)

Once connected and turned on the "Fix" LED on the gps board should start flashing red to indicate that it is looking for satellites. When it finds a lock then this will change to a solid green colour.

# Setting up the Pi to use

1. First we need to install the GPS drivers, and GPS service software so the Pi knows how to communicate with the GPS module. This install is ver large and can take a long time to install.
```
sudo apt-get install gpsd gpsd-clients
```

```
sudo killall gpsd
sudo gpsd /dev/serial0 -F /var/run/gpsd.sock
```

Try editing gpsd startup script
sudo pico /etc/default/gpsd
![image](https://github.com/user-attachments/assets/454ba20b-4e84-4ef3-a340-d36adaae49cf)


### Setting the System clock from the GPS Unit:
https://area-51.blog/2012/06/18/getting-gps-to-work-on-a-raspberry-pi/
Install NTP time server
```
sudo apt-get install ntp
```

sudo gpsinit -s 115200 -i set_system_clock /dev/serial0

Once the red flashing lock light goes out, check the GPS is recieving by using the following command:
```
cgps -s
```
This will display the current data from the GPS module which will look a bit like this:

<INSERT PICTURE OF CGPS OUTPUT>

### Troubleshooting
Raw GPS ouptut can be seen via running the gpsmon command and seeing if it outputs raw data from the device
```
gpsmon /dev/serial0
```
This will generate output like this:

![image](https://github.com/user-attachments/assets/8f86aec0-b076-4d87-a414-aaedffc55054)

It this keeps updating then the circuit is connected correctly

## Using the GPS in Python


1. ensure the python virtual environment module ins installed so we can create a new Virtual environment for python and install the required libraries
```
cd ~
sudo apt install python3-venv
```

2. Create a virtual environment
```
python3 -m venv env --system-site-packages
```

3. activate python virtual environment
```
cd ~
source env/bin/activate
```

4. Now install the Adafuit Blinka Library and ina230 library
```
pip3 install adafruit-circuitpython-gps
```
  

sudo pip3 install adafruit-circuitpython-gps
```
