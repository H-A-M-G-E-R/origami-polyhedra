# This hexagonal trapezohedron has eight kites with angles of 30, 105 and 120 degrees.
# Unlike John Montroll's design from https://johnmontroll.com/books/3d-origami-antidiamonds/, this one is mathematically correct.

import math
import turtle

def kite():
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(longLength*size)
    turtle.right(180-topAngle)
    turtle.forward(longLength*size)
    turtle.right(180-sideAngle)
    turtle.forward(shortLength*size)
    turtle.right(180-bottomAngle)
    turtle.forward(shortLength*size)
    turtle.right(180-sideAngle)
    turtle.end_fill()
    turtle.penup()

def gotoOnSquare(x, y):
    turtle.goto((-1+2*x)*squareRadius,(-1+2*y)*squareRadius)

topAngle = 30/180*math.pi # in radians
sideAngle = 105/180*math.pi
bottomAngle = 120/180*math.pi

shortLength = 1
longLength = math.cos(math.pi/2-bottomAngle/2)/math.cos(math.pi/2-topAngle/2)

angle = -math.pi/2+topAngle+sideAngle
x = shortLength*3.5*math.cos(angle)
angle -= math.pi-bottomAngle
x += shortLength*3*math.cos(angle)

ratio = 1/x

angle = -math.pi/2+topAngle+sideAngle
x = shortLength/2*math.cos(angle)
y = shortLength/2*math.sin(angle)
angle -= math.pi-bottomAngle
x += shortLength*math.cos(angle)
y += shortLength*math.sin(angle)

landmarks = [((1+x*ratio)/2, 0)]
extraLandmarks = [((1+x*ratio)/2, (1+y*ratio)/2)]
print(landmarks)

squareRadius = 400
size = squareRadius*ratio

topAngle = 30 # in degrees
sideAngle = 105
bottomAngle = 120

# Setup turtle
turtle.delay(0)
turtle.speed(0)
turtle.pensize(3)
turtle.color("#000000", "#BFBFBF")
#turtle.hideturtle()
turtle.penup()

# Draw net
for i in range(2):
    turtle.goto(0, 0)
    turtle.setheading(-90+topAngle+sideAngle+i*180)
    turtle.forward(shortLength/2*size)

    for j in range(2):
        turtle.setheading(90+i*180)

        kite()

        turtle.right(sideAngle)
        turtle.forward(shortLength*size)
        turtle.right(180-sideAngle)

        kite()

        turtle.left(topAngle+sideAngle)

        turtle.forward(shortLength*size)

    turtle.right(180-bottomAngle)
    turtle.forward(shortLength*size)
    turtle.right(180-sideAngle)

    kite()

    turtle.right(sideAngle)
    turtle.forward(shortLength*size)
    turtle.right(bottomAngle+sideAngle-180)

    kite()

# Draw square
turtle.setheading(0)
turtle.goto(-squareRadius,squareRadius)

turtle.pendown()
for i in range(4):
    turtle.forward(2*squareRadius)
    turtle.right(90)
turtle.penup()

# Draw landmarks
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

# Reference folds
turtle.pensize(2)

gotoOnSquare(0, 0)
turtle.pendown()
gotoOnSquare(1, 1)
turtle.penup()

gotoOnSquare(extraLandmarks[0][0], 0)
turtle.pendown()
gotoOnSquare(extraLandmarks[0][0], extraLandmarks[0][1])
turtle.penup()

turtle.exitonclick()
