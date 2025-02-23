# This pentagonal trapezohedron has a circumsphere. It has ten kites with angles of 51.83, 90 and 128.17 degrees.
# Unlike John Montroll's design from https://johnmontroll.com/books/3d-origami-antidiamonds/, this one is mathematically correct.
 
import math
import turtle

def kite():
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(longLength*size)
    turtle.right(180-topAngle)
    turtle.forward(longLength*size)
    turtle.right(90)
    turtle.forward(shortLength*size)
    turtle.right(180-bottomAngle)
    turtle.forward(shortLength*size)
    turtle.right(90)
    turtle.end_fill()
    turtle.penup()

landmarks = []

topAngle = 0.9045568943023813 # in radians
bottomAngle = math.pi-topAngle
longLength = 1.5302420679421518
shortLength = 0.7434960689203689

x = shortLength/2
y = longLength*2

landmarks.append((1-(1-x/y)/2, 0)) # The landmark is found at (0.5607335339695807, 0).

print(landmarks)

size = 150

turtle.delay(0)
turtle.speed(0)
turtle.pensize(3)
turtle.color("#000000", "#BFBFBF")
turtle.hideturtle()
turtle.penup()

topAngle = 51.82729237298775 # in degrees
bottomAngle = 180-topAngle

# The kites
for i in range(2):
    turtle.setheading(i*180)
    turtle.goto(0,0)
    turtle.backward(shortLength/2*size)
    turtle.left(90)

    kite()

    turtle.right(90)
    turtle.forward(shortLength*size)
    turtle.left(180-bottomAngle)
    turtle.forward(shortLength*size)
    turtle.setheading(90+i*180)

    kite()

    turtle.right(90)
    turtle.forward(shortLength*size)
    turtle.right(90)

    kite()

    turtle.left(90+180-bottomAngle)
    turtle.forward(shortLength*size)
    turtle.right(180-bottomAngle)
    turtle.forward(shortLength*size)
    turtle.right(90)
    if i == 0:
        squareRadius = turtle.pos()[0]

    kite()

    turtle.right(90)
    turtle.forward(shortLength*size)
    turtle.right(90+bottomAngle-180)

    kite()

# The square
squareRadius = 2*longLength*size
turtle.setheading(0)
turtle.goto(-squareRadius,squareRadius)

turtle.pendown()
for i in range(4):
    turtle.forward(2*squareRadius)
    turtle.right(90)
turtle.penup()

# Landmarks
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

turtle.exitonclick()
