import signal
import time

#http://stackoverflow.com/questions/2292054/python-timer-mystery
# Was having trouble with getting the interrupts to work properly, so i tried to follow this example i found online.

def interrupt(signum, _):
	print 'InterruptTime: ', time.time()

signal.signal(signal.SIGALRM, interrupt)
signal.setitimer(signal.ITIMER_REAL, .2, .2)

while(1):
	time.sleep(5)
	print 'Time2: ', time.time()
	print
