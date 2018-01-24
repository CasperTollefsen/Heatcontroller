# Heatcontroller
This is a program for controlling my heater through a Raspberry Pi.

IMPORTANT:
When working on the code all lines related to `GPIO` must be commented out. A system printout has been provided to display when the `GPIO` has been initiated.

- Open `resources.py`.
- Comment out `import RPi.GPIO as GPIO`.
- Navigate to `def heatController ():` and comment out all lines except the printout.