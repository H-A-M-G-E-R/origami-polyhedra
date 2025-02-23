# This heptagonal trapezohedron has a circumsphere. It has fourteen kites with angles of 36.68, 90 and 143.32 degrees.

import math
import turtle

landmarks = []

topAngle = 0.6402645599752099 # in radians
bottomAngle = math.pi-topAngle
longLength = 2.18766852347925
shortLength = 0.7252913495974176

landmarks.append(((1-math.tan(math.pi/4-topAngle))/2, 0)) # The first landmark is found at (0.42691935852751817, 0).

x = longLength+shortLength+longLength
y = longLength-shortLength+longLength

landmarks.append((0, (1-y/x)/2)) # The second landmark is found at (0, 0.14219646937760722).

print(landmarks)

size = 100

turtle.delay(0)
turtle.speed(0)
turtle.pensize(3)
turtle.color("#000000", "#BFBFBF")
turtle.hideturtle()
turtle.penup()

topAngle = 36.6844570583803 # in degrees
bottomAngle = 180-topAngle

for i in range(4):
    turtle.setheading(45+topAngle+i*90)
    turtle.goto(0,0)

    if not i == 3:
        turtle.pendown()
        turtle.begin_fill()
        turtle.forward(longLength*size)
        turtle.right(90)
        turtle.forward(shortLength*size)
        turtle.right(180-bottomAngle)
        turtle.forward(shortLength*size)
        turtle.right(90)
        turtle.forward(longLength*size)
        turtle.right(180-topAngle)
        turtle.end_fill()
        turtle.penup()

    turtle.right(topAngle)

    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(longLength*size)
    turtle.right(90)
    turtle.forward(shortLength*size)
    turtle.right(180-bottomAngle)
    turtle.forward(shortLength*size)
    turtle.right(90)
    turtle.forward(longLength*size)
    turtle.right(180-topAngle)
    turtle.end_fill()
    turtle.penup()

    turtle.forward(longLength*size)
    turtle.right(90)
    turtle.forward(shortLength*size)
    turtle.right(180)

    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(shortLength*size)
    turtle.right(180-bottomAngle)
    turtle.forward(shortLength*size)
    turtle.right(90)
    turtle.forward(longLength*size)
    turtle.right(180-topAngle)
    turtle.forward(longLength*size)
    turtle.right(90)
    turtle.end_fill()
    turtle.penup()

    turtle.right(90)
    turtle.forward(longLength*size)
    turtle.right(180-topAngle)
    if i == 0:
        squareRadius = turtle.pos()[0]
    else:
        turtle.pendown()
        turtle.begin_fill()
        turtle.forward(longLength*size)
        turtle.right(90)
        turtle.forward(shortLength*size)
        turtle.right(180-bottomAngle)
        turtle.forward(shortLength*size)
        turtle.right(90)
        turtle.forward(longLength*size)
        turtle.right(180-topAngle)
        turtle.end_fill()
        turtle.penup()

turtle.setheading(0)
turtle.goto(-squareRadius,squareRadius)

turtle.pendown()
for i in range(4):
    turtle.forward(2*squareRadius)
    turtle.right(90)
turtle.penup()

turtle.setheading(270)
i = 1
for (x, y) in landmarks:
    turtle.goto((-1+2*x)*squareRadius,(-1+2*y)*squareRadius)
    turtle.dot(20)
    turtle.forward(45)
    turtle.write(f"p{i}", align="center", font=("Arial", 25, "normal"))

    turtle.goto(-squareRadius,-squareRadius)
    turtle.forward(60+i*40)
    turtle.write(f"p{i} = ({x}, {y})", align="left", font=("Arial", 25, "normal"))

    i += 1

turtle.pensize(2)

turtle.goto(-squareRadius,-squareRadius)
turtle.pendown()
turtle.goto(squareRadius,squareRadius)
turtle.penup()

turtle.goto(-squareRadius,squareRadius)
turtle.pendown()
turtle.goto(squareRadius,-squareRadius)
turtle.penup()

turtle.goto(0,0)
turtle.pendown()
turtle.goto((-1+2*landmarks[0][0])*squareRadius,(-1+2*landmarks[0][1])*squareRadius)
turtle.penup()

turtle.exitonclick()
