#Axiom F+F+F+F
#F --> FF+F-F+F+FF
#ø = 90 


import turtle

def instructions(iterations, axiom):
	StartString =  axiom
	EndString = ""
	for i in range(iterations):
		EndString = ProcessString(StartString)
		StartString = EndString
	
	return EndString

def ProcessString(OldString):
	NewString = ""
	for ch in OldString:
		
		NewString = NewString + ApplyRules(ch)
	return NewString


def ApplyRules(ch):
	NewString = ""
	if ch == "F":
		NewString = "F+F-F-F+F"
	else: 
		NewString = ch
	
	return NewString


def DrawSystem(t, instructions, angle, distance):	
	
	for cmd in instructions:
		if cmd == "F":
			t.forward(distance)
		elif cmd == "B":
			t.backward(distance)
		elif cmd == "+":
			t.right(angle)
		elif cmd == "-":
			t.left(angle)

def main():
	instr = instructions(5, "FF+FF+FF+FF")
	
	t = turtle.Turtle()
	wn = turtle.Screen()	
	
	t.speed = 15
	t.up()
	t.backward(200)
	t.down()
	DrawSystem(t, instr, 90, 10)

main()		
