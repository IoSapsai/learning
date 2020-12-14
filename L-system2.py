import turtle

def instructions(iters, axiom):
    startString = axiom
    endString = ""
    
    for i in range(iters): 
        endString = processString(startString)
        startString = endString
    return endString

def processString(oldString):
    newString = ''
    for ch in oldString: 
        newString = newString + applyRules(ch)
        
    return newString

def applyRules(ch):
    newString = ""
    if ch == "F":
        newString = "F[-F]F[+F]F"
    else:
        newString = ch
    return newString
def drawSystem(t, instr, distance, angle):
    saved_info_list = []
    for cmd in instr:
        if cmd == "F":
            t.forward(distance)
        elif cmd == "B":
            t.backward(distance)
        elif cmd == "+":
            t.right(angle)
        elif cmd == "-":
            t.left(angle)
        elif cmd == "[":
            saved_info_list.append([t.heading(), t.xcor(), t.ycor()])
        elif cmd == "]":
            new_info = saved_info_list.pop()
            t.setheading(new_info[0])
            t.setposition(new_info[1], new_info[2])

def main():
    tee = turtle.Turtle()
    wn = turtle.Screen()
    tee.speed(20)
    tee.up()
    tee.back(200)
    tee.down()
    
    instr = instructions(10, "F")
    drawSystem(tee, instr, 10, 25)

main()
        
