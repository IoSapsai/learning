#This program calculates the distance between two points, using the Pythagorean theorem.

import math
x1 = int(input("coordinate of the first x point"))
y1 = int(input("coordinate of the first y point"))
x2 = int(input("coordinate of the second x point"))
y2 = int(input("coordinate of the second y point"))

distance = math.sqrt (math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))

print (distance)
