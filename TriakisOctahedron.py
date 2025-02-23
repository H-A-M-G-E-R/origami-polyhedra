# Measures taken from https://en.wikipedia.org/wiki/Triakis_octahedron
import math
import turtle

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

smallAngle = math.acos(1/2+math.sqrt(2)/4) # in radians
largeAngle = math.acos(1/4-math.sqrt(2)/2)
shortLength = 2*math.sqrt(2)-2
longLength = math.sqrt(2)

# Calculate landmarks
x = longLength
y = 0

angle = math.pi-2*smallAngle
x += longLength*math.cos(angle)
y += longLength*math.sin(angle)

x += longLength

turn = math.atan(3/4)-math.atan(y/x)

landmarks = [((1-math.tan(math.pi/2-2*smallAngle-turn))/2, 0), ((1+math.tan(turn))/2, 0), (0, 1/8)]
print(landmarks)

smallAngle = math.acos(1/2+math.sqrt(2)/4)/math.pi*180 # in degrees
largeAngle = math.acos(1/4-math.sqrt(2)/2)/math.pi*180
turn = turn/math.pi*180

size = 200

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
    turtle.setheading(smallAngle+turn+i*90)

    triangle(shortLength, largeAngle, shortLength, smallAngle, longLength)

    turtle.left(smallAngle)

    triangle(longLength, smallAngle, shortLength, largeAngle, shortLength)

    turtle.right(smallAngle)
    turtle.forward(shortLength*size)
    turtle.left(largeAngle*2-180)

    triangle(shortLength, smallAngle, longLength, smallAngle, shortLength)

    turtle.forward(shortLength*size)
    turtle.setheading(turn+i*90)

    triangle(longLength, smallAngle, shortLength, largeAngle, shortLength)

    turtle.right(smallAngle)

    triangle(shortLength, largeAngle, shortLength, smallAngle, longLength)

    turtle.left(smallAngle)
    turtle.forward(longLength*size)
    turtle.right(180-smallAngle*2)

    triangle(longLength, smallAngle, shortLength, largeAngle, shortLength)

    if i == 0:
        squareRadius = turtle.pos()[0]

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
gotoOnSquare(1-landmarks[0][0], 1)
turtle.penup()

gotoOnSquare(landmarks[1][0], 0)
turtle.pendown()
gotoOnSquare(1-landmarks[1][0], 1)
turtle.penup()

turtle.exitonclick()
