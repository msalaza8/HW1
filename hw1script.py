#! /usr/bin/python
# coding: utf-8

import math


def EndEffectorCalculator(a1, a2, a3):
  
  xTotal = float(1*math.cos(rad1) + 3*math.cos(rad1 + rad2) + 2*math.cos(rad1 + rad2 + rad3))
  print
  print(xTotal)

  yTotal =  float(1*math.sin(rad1) + 3*math.sin(rad1 + rad2) + 2*math.sin(rad1 + rad2 + rad3))
  print(yTotal)

  EndEffector = math.sqrt(xTotal*xTotal + yTotal*yTotal)
  print
  print(EndEffector)
  print


x = raw_input()
angle1 = float(x)
rad1 = math.radians(angle1)

y = raw_input()
angle2 = float(y)
rad2 = math.radians(angle2)

z = raw_input()
angle3 = float(z)
rad3 = math.radians(angle3)


EndEffectorCalculator(rad1, rad2, rad3)




