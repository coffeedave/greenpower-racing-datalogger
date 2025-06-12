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
