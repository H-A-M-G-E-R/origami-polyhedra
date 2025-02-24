# This square trapezohedron has eight kites with angles of 45, 112.5 and 90 degrees.
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

topAngle = math.pi/4 # in radians
bottomAngle = math.pi/2
sideAngle = math.pi-topAngle/2-bottomAngle/2

shortLength = 1
longLength = math.sqrt(2+math.sqrt(2))

angle = -math.pi/2+topAngle+sideAngle
x = shortLength*1.5*math.cos(angle)
angle -= bottomAngle
x += shortLength*2*math.cos(angle)

angle = -math.pi/2+topAngle+sideAngle
y = -shortLength/2*math.sin(angle)
angle -= sideAngle
y += 2*longLength*math.sin(angle)

ratio = 1/((x-y)/2)

angle = -math.pi/2+topAngle+sideAngle
x = -shortLength/2*math.cos(angle)
y = -shortLength/2*math.sin(angle)

landmarks = [((1+x*ratio)/2+(1+y*ratio)/2, 0), (1-math.sqrt(2)/2, 0)]
extraLandmarks = [((1+x*ratio)/2, (1+y*ratio)/2)]

print(landmarks)

squareRadius = 400
size = squareRadius*ratio

topAngle = 45 # in degrees
bottomAngle = 90
sideAngle = 112.5

# Setup turtle
turtle.delay(0)
turtle.speed(0)
turtle.pensize(3)
turtle.color("#000000", "#BFBFBF")
turtle.hideturtle()
turtle.penup()

# Draw net
for i in range(2):
    turtle.goto(0, 0)
    turtle.setheading(-90+topAngle+sideAngle+i*180)
    turtle.forward(shortLength/2*size)
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

gotoOnSquare(landmarks[0][0], 0)
turtle.pendown()
gotoOnSquare(extraLandmarks[0][0], extraLandmarks[0][1])
turtle.penup()

gotoOnSquare((1+landmarks[0][0])/2, 0)
turtle.pendown()
gotoOnSquare((1+landmarks[0][0])/2, 1)
turtle.penup()

gotoOnSquare((1-landmarks[0][0])/2, 0)
turtle.pendown()
gotoOnSquare((1-landmarks[0][0])/2, 1)
turtle.penup()

gotoOnSquare(1-math.sqrt(2)/2, 0)
turtle.pendown()
gotoOnSquare(math.sqrt(2)/2, 1)
turtle.penup()

turtle.exitonclick()
