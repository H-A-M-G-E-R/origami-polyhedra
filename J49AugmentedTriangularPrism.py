# https://en.wikipedia.org/wiki/Augmented_triangular_prism

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

squareRadius = 400
size = squareRadius*(1-math.sqrt(3)/3)*math.sqrt(2)

turtle.delay(0)
turtle.speed(0)
turtle.pensize(3)
turtle.color("#000000", "#BFBFBF")
turtle.hideturtle()
turtle.penup()

# Draw net
for i in range(2):
    turtle.goto(0, 0)
    turtle.setheading(75+i*180)

    polygon(3)

    turtle.forward(size)
    turtle.right(30)

    polygon(4)

    turtle.goto(0, 0)
    turtle.setheading(75+90+i*180)

    polygon(3)

    turtle.forward(size)
    turtle.right(60)

    polygon(3)

# Calculate landmark
landmarks = [((1-(2-math.sqrt(3)))/2, 0)] # 2-math.sqrt(3) = tan(15°)
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

# Draw square
turtle.setheading(0)
turtle.goto(-squareRadius,squareRadius)

turtle.pendown()
for i in range(4):
    turtle.forward(2*squareRadius)
    turtle.right(90)
turtle.penup()

# Reference folds
turtle.pensize(2)

gotoOnSquare(1/2, 0)
turtle.pendown()
gotoOnSquare(1/2, 1)
turtle.penup()

gotoOnSquare(0, 1/2)
turtle.pendown()
gotoOnSquare(1, 1/2)
turtle.penup()


gotoOnSquare((1-(2-math.sqrt(3)))/2, 0)
turtle.pendown()
gotoOnSquare((1+(2-math.sqrt(3)))/2, 1)
turtle.penup()

gotoOnSquare((1+(2-math.sqrt(3)))/2, 0)
turtle.pendown()
gotoOnSquare((1-(2-math.sqrt(3)))/2, 1)
turtle.penup()

gotoOnSquare(0, (1-(2-math.sqrt(3)))/2)
turtle.pendown()
gotoOnSquare(1, (1+(2-math.sqrt(3)))/2)
turtle.penup()

gotoOnSquare(0, (1+(2-math.sqrt(3)))/2)
turtle.pendown()
gotoOnSquare(1, (1-(2-math.sqrt(3)))/2)
turtle.penup()


gotoOnSquare((1-(2-math.sqrt(3)))/2, 0)
turtle.pendown()
gotoOnSquare(1, (1+(2-math.sqrt(3)))/2)
turtle.penup()

gotoOnSquare((1+(2-math.sqrt(3)))/2, 0)
turtle.pendown()
gotoOnSquare(0, (1+(2-math.sqrt(3)))/2)
turtle.penup()

gotoOnSquare((1-(2-math.sqrt(3)))/2, 1)
turtle.pendown()
gotoOnSquare(1, (1-(2-math.sqrt(3)))/2)
turtle.penup()

gotoOnSquare((1+(2-math.sqrt(3)))/2, 1)
turtle.pendown()
gotoOnSquare(0, (1-(2-math.sqrt(3)))/2)
turtle.penup()

turtle.exitonclick()
