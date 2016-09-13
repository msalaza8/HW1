import time
import math

def EndEffectorCalculator(a1, a2, a3):
	xTotal = float(1*math.cos(a1) + 3*math.cos(a1 + a2) + 2*math.cos(a1 + a2 + a3))

  	yTotal =  float(1*math.sin(a1) + 3*math.sin(a1 + a2) + 2*math.sin(a1 + a2 + a3))

  	EndEffector = math.sqrt(xTotal*xTotal + yTotal*yTotal)	

while(1):
	count = 0

	t0 = time.time()
	EndEffectorCalculator(45, 0, 30)
	t1 = time.time()

	print 'Delta T = ', t1 - t0
	print 'Clock = ', time.clock()

	while(count < 15500000):
		count = count + 1
