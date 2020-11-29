#Makes turtle draw a trippy square within square within square (and so on)

import turtle

def drawSquare(t, sz):
    for i in range(4):        
        t.forward(sz)
        t.left(90)
	
    t.penup()
    
    t.forward(sz+10)
    t.right(90)
    t.forward(10)
    t.left(180)
    
    t.pendown()
        

trippy = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor("black")
trippy.pensize(6)
trippy.color("fuchsia")
a = 20
trippy.speed(5)
for i in range (50):
    drawSquare(trippy, a)
    a = a+20
    
wn.exitonclick()
