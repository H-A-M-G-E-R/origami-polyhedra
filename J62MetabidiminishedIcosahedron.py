# https://en.wikipedia.org/wiki/Metabidiminished_icosahedron

import math
import turtle

def polygon(n, scale=1):
    turtle.pendown()
    turtle.begin_fill()
    for i in range(n):
        turtle.forward(scale*size)
        turtle.right(360/n)
    turtle.end_fill()
    turtle.penup()

def gotoOnSquare(x, y):
    turtle.goto((-1+2*x)*squareRadius,(-1+2*y)*squareRadius)

ratio = 2/math.sqrt(3)/5
squareRadius = 400
size = squareRadius*2*ratio

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
    turtle.setheading(-30+i*180)
    turtle.forward(size/2)
    turtle.right(60)

    polygon(3)

    turtle.right(60)

    polygon(3)

    turtle.forward(size)
    turtle.right(60)

    polygon(3)

    turtle.left(108)

    polygon(5)

    turtle.right(108)
    turtle.forward(size)

    polygon(3)

    turtle.right(60)

    polygon(3)

# Draw square
turtle.setheading(0)
turtle.goto(-squareRadius,squareRadius)

turtle.pendown()
for i in range(4):
    turtle.forward(2*squareRadius)
    turtle.right(90)
turtle.penup()

# Calculate landmarks
x1 = 1/2
y1 = 1/2
angle = -120*math.pi/180

x1 += math.sqrt(3)/2*ratio*math.cos(angle)
y1 += math.sqrt(3)/2*ratio*math.sin(angle)

angle -= math.pi/2
angle += 72*math.pi/180

x1 += (1+math.sqrt(5))/2*ratio*math.cos(angle)
y1 += (1+math.sqrt(5))/2*ratio*math.sin(angle)

landmarks = [(x1+y1*math.sqrt(3), 0)]
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

gotoOnSquare(landmarks[0][0], 0)
turtle.pendown()
gotoOnSquare(0, x1/math.sqrt(3)+y1)
turtle.penup()

turtle.exitonclick()
