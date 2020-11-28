import math

pi = 3
a = 2
b = 3
c = 4

for i in range (100):
	
	pi = pi + (4 * ((-1)**i)) / (a * b * c)
	a = a + 2
	b = b + 2
	c = c + 2
print (pi)

print (math.pi)

