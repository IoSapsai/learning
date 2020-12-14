#chapter 2
#problem 1
print(5 ** 2)
print (9 * 5)
print (15 / 12)
print (12 / 15)
print (15 // 12)
print (12 // 15)
print (5 % 2)
print (9 % 5)
print (15 % 12)
print (12 % 15)
print (6 % 6)
print (0 % 7)

#problem 2
2 + (3 - 1) * 10 / 5 * (2 + 3)
print (2 + (3 - 1) * 10 / 5 * (2 + 3))

#problem 3

day = 24
time = int(input("What time is it now?"))
alarm = int(input("In how many hours should the alarm ring?"))
ring = (time + alarm) % day
print ("The next alarm will ring at" , ring)

#problem 4


#Sunday = 0
#Monday = 1
#Tuesday = 2
#Wednesday = 3
#Thursday = 4
#Friday = 5
#Saturday = 6
depart = int(input("On which day of the week are you going on holiday?"))
stay = int(input("How many days are you staying?"))
home = (stay + depart) % 7
print ("You will return home on day" , home , "of the week, where 0 is Sunday, and 6 is Saturday.")

#problem 5
a = "All"
b = "work"
c = "and"
d = "no"
e = "play"
f = "makes"
g = "Jack"
h = "a"
i = "dull"
j = "boy."
print (a,b,c,d,e,f,g,h,i,j)

#problem 6
n=(6 * (1 - 2))
print (n)

#problem 7
P = 10000
n = 12
r = 0.08
t = int (input("Please type in the number of years, that the money will be compounded for"))
A = P * ( ((1 + (r/n)) ** (n * t)) )
print ("The final amount after" , t , "years is" , A , ".")

#problem 8
pi = 3.1415
r = int(input("What is the radius of the circle in cm? (The distance from the center to the edge)"))
A = pi * r ** 2
print ("The area of your circle, my dear user, is" , A , "square cm")

#problem 9
a = int(input("What is the height of your rectangle in cm?"))
b = int(input("What is the width of your rectangle in cm?"))
S = a * b
print ("The area of your fine and beautiful rectangle is" , S , "square cm.")

#problem 10

M = int(input("How many miles have you traveled?"))
G = int(input("How many much fuel in gallons have you burned during that time?"))
MPG = M / G
print ("Your car runs at" , MPG , "miles per gallon. Also I have no idea about freedom units.")

#problem 11

C = int(input("how many degrees C° would you like to convert?"))
F = (C * 9 / 5 + 32)
print (C , "degrees Celsius is equal to" , F , "degrees Farenheit.")

#problem 12

F = float(input("How many degrees F° would you like to convert"))
C = (F - 32) * 5 / 9
print (F , "degrees farenheit is" , C , "degrees celsius.")

