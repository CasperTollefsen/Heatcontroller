from time import sleep, localtime, strftime
#import RPi.GPIO as GPIO

def heatController():
	# GPIO.setmode(GPIO.BOARD)
	# GPIO.setup(11, GPIO.OUT)

	# GPIO.output(11, True)
	# sleep(0.5)
	# GPIO.output(11, False)

	# GPIO.cleanup()

	print "\n[SYSTEM] Heatcontroller initiated [%s]\n" % (strftime("%H:%M:%S", localtime()))

def stringConverter(number):
	if (number == 0):
		number = "00"
	elif (number < 10):
		number = "0" + str(number)
	else:
		number = str(number)
	return number

def timeConverter(start, end):

	h = 0
	m = 0
	s = int(end - start)

	while (s > 60):
		m = m + 1
		s = s - 60
	while (m > 60):
		h = h + 1
		m = m - 60

	return stringConverter(h) + ":" + stringConverter(m) + ":" + stringConverter(s)
