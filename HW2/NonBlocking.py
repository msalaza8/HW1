import time
import math

def EndEffectorCalculator(a1, a2, a3):
	xTotal = float(1*math.cos(a1) + 3*math.cos(a1 + a2) + 2*math.cos(a1 + a2 + a3))

  	yTotal =  float(1*math.sin(a1) + 3*math.sin(a1 + a2) + 2*math.sin(a1 + a2 + a3))

  	EndEffector = math.sqrt(xTotal*xTotal + yTotal*yTotal)	

while(1):

	T0 = time.time()
	EndEffectorCalculator(45, 0, 30)
	T1 = time.time()

	time.sleep(1 - (T1 - T0))

	print 'Delta T = ', T1 - T0
	print 'Clock = ', time.clock()
