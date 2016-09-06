#! /usr/bin/python
# coding: utf-8

import math


x = raw_input()
angle1 = float(x)
rad1 = math.radians(angle1)
print(rad1)
angle1 = (math.cos(math.radians(angle1)))
print(angle1)

y = raw_input()
angle2 = float(y)
rad2 = math.radians(angle2)
print(rad2)
angle2 = (math.cos(math.radians(angle2)))
print(angle2)

z = raw_input()
angle3 = float(z)
rad3 = math.radians(angle3)
print(rad3)
angle3 = (math.cos(math.radians(angle3)))
print(angle3)




xTotal = float(1*math.cos(rad1) + 3*math.cos(rad1 + rad2) + 2*math.cos(rad1 + rad2 + rad3))
