from time import localtime, strftime, sleep, time
import resources

# Time to wake up
wakeupTime = "11:21:30"

# Minutes between each check
cycleReset_interval = 0.1

startTime = strftime("%a, %d %b %Y [%H:%M:%S]")
weekDay = strftime("%a", localtime())
run = True
cycleReset = 0
startTimer = time()
cycleTime = time()

print "[SYSTEM STATUS]\nTime started:\t%s\nTarget time:\t%s\n" % (startTime, wakeupTime)

while (run == True):
	if (strftime("%H:%M:%S", localtime()) >= wakeupTime):
		resources.heatController()
		run = False
	else:
		print "[SYSTEM] Running cycle %4.1d [%s] (%s)" % (cycleReset, strftime("%H:%M:%S"), resources.timeConverter(cycleTime, time()))
		cycleTime = time()
		cycleReset = cycleReset + 1
		sleep(60 * cycleReset_interval)

print "[SYSTEM STATUS]\nStarted:\t%s\nTarget time:\t%s\nTotal runtime:\t%s\nTotal cycles:\t%d\nEnded:\t\t%s\n" % (startTime, wakeupTime, resources.timeConverter(startTimer, time()), cycleReset, strftime("%a, %d %b %Y [%H:%M:%S]"))
