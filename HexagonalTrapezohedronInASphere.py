# This hexagonal trapezohedron has a circumsphere. It has twelve kites with angles of 42.94, 90 and 137.06 degrees.
 
import math
import turtle

landmarks = []

topAngle = 0.74946886541748 # in radians
bottomAngle = math.pi-topAngle
longLength = 1.8612097182041996
shortLength = 0.7320508075688773

landmarks.append((1-(1-math.tan(math.pi/2-2*topAngle))/2, 0)) # The first landmark is found at (0.5359912681803607, 0).

angle = math.pi/2-topAngle
x = math.cos(angle)*longLength
y = math.sin(angle)*longLength

angle -= math.pi/2
x += math.cos(angle)*shortLength
y += math.sin(angle)*shortLength

angle += math.pi/2
x += math.cos(angle)*longLength
y += math.sin(angle)*longLength

landmarks.append((0, (1-y/x)/2)) # The second landmark is found at (0, 0.13762405515603876).

print(landmarks)

size = 100

turtle.delay(0)
turtle.speed(0)
turtle.pensize(3)
turtle.color("#000000", "#BFBFBF")
turtle.hideturtle()
turtle.penup()

topAngle = 42.941402864879905 # in degrees
bottomAngle = 180-topAngle

for i in range(3):
    turtle.setheading(90+i*90)
    turtle.goto(0,0)

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

turtle.goto(-squareRadius,0)
turtle.pendown()
turtle.goto(squareRadius,0)
turtle.penup()

turtle.goto(0,-squareRadius)
turtle.pendown()
turtle.goto(0,squareRadius)
turtle.penup()

turtle.goto((-1+2*landmarks[0][0])*squareRadius,(-1+2*landmarks[0][1])*squareRadius)
turtle.pendown()
turtle.goto((-1+2*landmarks[0][0])*-squareRadius,(-1+2*landmarks[0][1])*-squareRadius)
turtle.penup()

turtle.exitonclick()
