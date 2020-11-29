#This is the same distance calculator, written methodically, without using the math module. Yields same results. The formula is more of a step-by-step calculation.


x1 = int(input("coordinate of the first x point"))
y1 = int(input("coordinate of the first y point"))
x2 = int(input("coordinate of the second x point"))
y2 = int(input("coordinate of the second y point"))
dx = (x2 - x1)
dy = (y2 - y1)
dxsquared = dx**2
dysquared = dy**2
result = (dxsquared + dysquared)**0.5

print (result)
