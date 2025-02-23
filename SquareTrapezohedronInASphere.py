# This square trapezohedron has a circumsphere. It has eight kites with angles of 65.53, 90 and 114.47 degrees.

import math
import turtle

def gotoOnSquare(x, y):
    turtle.goto((-1+2*x)*squareRadius,(-1+2*y)*squareRadius)

halfWidth = math.sqrt(math.sqrt(2)-1) # Given a kite with heights 1 and sqrt(2)-1, this gives a circumscribable kite.
longLength = math.sqrt(math.sqrt(2))
shortLength = math.sqrt(2-math.sqrt(2))
topAngle = math.atan(halfWidth)*2
bottomAngle = math.pi-topAngle # 180 degrees - top angle

# Calculate landmarks
landmarks = [(0.5-math.tan((math.pi/2-topAngle)/2)/2, 0)] # The first landmark is found at (0.27245506971888644, 0).

x = 0
y = 0
angle = topAngle+(math.pi/2-topAngle)/2

x += longLength*math.cos(angle)
y += longLength*math.sin(angle)

angle -= math.pi/2
x += shortLength*math.cos(angle)
y += shortLength*math.sin(angle)

angle += math.pi/2
x += longLength*math.cos(angle)
y += longLength*math.sin(angle)

landmarks.append((0.5-(x/y)/2, 0)) # The second landmark is found at (0.04491013943777261, 0).

print(landmarks)

squareRadius = 400
size = squareRadius/y

# Setup turtle
turtle.delay(0)
turtle.speed(0)
turtle.pensize(3)
turtle.color("#000000", "#BFBFBF")
turtle.hideturtle()
turtle.penup()

topAngle = topAngle/math.pi*180 # convert to degrees
bottomAngle = 180-topAngle

# Draw net
for i in range(4):
    turtle.setheading(topAngle+(90-topAngle)/2+i*90)
    turtle.goto(0, 0)

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
    turtle.right(180-90-bottomAngle)

    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(shortLength*size)
    turtle.right(90)
    turtle.forward(longLength*size)
    turtle.right(180-topAngle)
    turtle.forward(longLength*size)
    turtle.right(90)
    turtle.forward(shortLength*size)
    turtle.right(180-bottomAngle)
    turtle.end_fill()
    turtle.penup()

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
gotoOnSquare(1-landmarks[0][0], 1)
turtle.penup()

gotoOnSquare(1-landmarks[0][0], 0)
turtle.pendown()
gotoOnSquare(landmarks[0][0], 1)
turtle.penup()

turtle.exitonclick()
