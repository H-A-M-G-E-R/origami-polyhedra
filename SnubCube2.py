# Yields a larger snub cube than SnubCube.py, but there's a cross at the bottom.

import math
import turtle

def polygon(n, scale=1, fill=True):
    turtle.pendown()
    if fill:
        turtle.begin_fill()
    for i in range(n):
        turtle.forward(scale*size)
        turtle.right(360/n)
    turtle.end_fill()
    turtle.penup()

def triangle(l1, a1, l2, a2, l3):
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(l1*size)
    turtle.right(180-a1)
    turtle.forward(l2*size)
    turtle.right(180-a2)
    turtle.forward(l3*size)
    turtle.right(a1+a2)
    turtle.end_fill()
    turtle.penup()

def gotoOnSquare(x, y):
    turtle.goto((-1+2*x)*squareRadius,(-1+2*y)*squareRadius)

def lineOnSquare(x1, y1, x2, y2):
    gotoOnSquare(x1, y1)
    turtle.pendown()
    gotoOnSquare(x2, y2)
    turtle.penup()

size = 100

# Setup turtle
turtle.delay(0)
turtle.speed(0)
turtle.pensize(3)
turtle.color("#000000", "#BFBFBF")
turtle.hideturtle()
turtle.penup()

# Draw net
for i in range(4):
    turtle.goto(0, 0)
    turtle.setheading(15+i*90)
    turtle.forward(math.sqrt(2)/2*size)
    turtle.right(135)

    polygon(4)

    turtle.left(60)

    polygon(3)

    turtle.left(60)

    polygon(3)

    turtle.forward(size)
    turtle.right(60)

    polygon(3)

    turtle.left(60)

    polygon(3)

    turtle.forward(size)
    turtle.right(60)

    polygon(3)
    if i == 0:
        turtle.forward(size)
        squareRadius = abs(turtle.pos()[0])
        turtle.backward(size)

    turtle.right(120)
    turtle.forward(2*size)
    turtle.right(90)

    polygon(3)

    turtle.forward(size)
    turtle.right(30)

    polygon(4)

    turtle.forward(size)
    turtle.right(30)

    polygon(3)

    turtle.forward(size)
    turtle.right(60)

    polygon(3)

    turtle.forward(size)
    turtle.left(180)

    triangle(1, 45, math.sqrt(2)/2, 90, math.sqrt(2)/2)
    turtle.pensize(3)

    turtle.right(90)
    turtle.forward(size)

# Draw square
turtle.setheading(0)
turtle.goto(-squareRadius,squareRadius)

turtle.pendown()
for i in range(4):
    turtle.forward(2*squareRadius)
    turtle.right(90)
turtle.penup()

# Calculate landmark
x = math.sqrt(2)/2*math.cos(math.pi/12)+2.5
x2 = math.sqrt(2)/2*math.cos(math.pi/12)

landmarks = [((1-x2/x)/2, 0)] # The landmark is located at (0.40968042307871194, 0).
print(landmarks)

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

lineOnSquare((1+(2-math.sqrt(3)))/2, 0, (1-(2-math.sqrt(3)))/2, 1)
lineOnSquare(0, (1-(2-math.sqrt(3)))/2, 1, (1+(2-math.sqrt(3)))/2)

lineOnSquare(landmarks[0][0], landmarks[0][1], landmarks[0][0], 0.25)

turtle.exitonclick()
