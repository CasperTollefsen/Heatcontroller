# Heatcontroller
This is a program for controlling an Adax heater through Raspberry Pi 3 model B.

IMPORTANT:
When working on the code all lines related to `GPIO` must be commented out. A system printout has been provided to display when the `GPIO` has been initiated.

INSTRUCTIONS:
1.	Open `resources.py`.
2.	Comment out `import RPi.GPIO as GPIO`.
3.	Navigate to `def heatController ():` and comment out all lines except the printout.

NOTE:
Remember to revert comment process before commit/push.