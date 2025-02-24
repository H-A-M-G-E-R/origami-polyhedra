# The lighter gray triangles are the nonsunken sides and the darker gray triangles are in sunken sides.
import math
import turtle

def triangle(l1, a1, l2, a2, l3, color=None):
    if color != None:
        turtle.fillcolor(color)
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

mediumAngle = math.atan(math.sqrt(2))/math.pi*180 # in degrees
largeAngle = 180-2*mediumAngle
smallAngle = largeAngle/2

sizeRatio = 8+2*math.sqrt(2)
squareRadius = 400
size = squareRadius*2/sizeRatio

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
    turtle.setheading(90+i*180)

    triangle(1, 90, math.sqrt(2), smallAngle, math.sqrt(3), "#7F7F7F")
    turtle.right(mediumAngle)
    triangle(math.sqrt(3), mediumAngle, 2, mediumAngle, math.sqrt(3), "#BFBFBF")
    turtle.right(largeAngle)
    triangle(math.sqrt(3), smallAngle, math.sqrt(2), 90, 1, "#7F7F7F")

    turtle.forward(math.sqrt(3)*size)
    turtle.left(180-mediumAngle)

    triangle(2, 45, math.sqrt(2), 90, math.sqrt(2), "#7F7F7F")
    turtle.right(45)
    triangle(math.sqrt(2), 90, 1, mediumAngle, math.sqrt(3), "#7F7F7F")
    turtle.right(smallAngle)
    triangle(math.sqrt(3), largeAngle, math.sqrt(3), mediumAngle, 2, "#BFBFBF")

    turtle.forward(math.sqrt(3)*size)
    turtle.left(180-mediumAngle)

    triangle(1, 90, math.sqrt(2), smallAngle, math.sqrt(3), "#7F7F7F")
    turtle.right(mediumAngle)
    triangle(math.sqrt(3), mediumAngle, 2, mediumAngle, math.sqrt(3), "#BFBFBF")
    turtle.right(largeAngle)
    triangle(math.sqrt(3), smallAngle, math.sqrt(2), 90, 1, "#7F7F7F")
    turtle.right(mediumAngle)
    triangle(1, 90, math.sqrt(2), smallAngle, math.sqrt(3), "#7F7F7F")

    turtle.forward(size)

    triangle(math.sqrt(2), 45, 2, 45, math.sqrt(2), "#7F7F7F")

    turtle.forward(math.sqrt(2)*size)
    turtle.right(180-45-mediumAngle)

    triangle(math.sqrt(3), largeAngle, math.sqrt(3), mediumAngle, 2, "#BFBFBF")

    turtle.goto(0, 0)
    turtle.setheading(90+i*180)
    turtle.forward(size)

    triangle(math.sqrt(2), 45, 2, 45, math.sqrt(2), "#7F7F7F")

    turtle.forward(math.sqrt(2)*size)

    triangle(2, 45, math.sqrt(2), 90, math.sqrt(2), "#7F7F7F")
    turtle.right(45)
    triangle(math.sqrt(2), 90, 1, mediumAngle, math.sqrt(3), "#7F7F7F")
    turtle.right(smallAngle)
    triangle(math.sqrt(3), largeAngle, math.sqrt(3), mediumAngle, 2, "#BFBFBF")

    turtle.forward(math.sqrt(3)*size)
    turtle.left(180-mediumAngle)

    triangle(1, 90, math.sqrt(2), smallAngle, math.sqrt(3), "#7F7F7F")
    turtle.right(mediumAngle)
    triangle(math.sqrt(3), mediumAngle, 2, mediumAngle, math.sqrt(3), "#BFBFBF")
    turtle.right(largeAngle)
    triangle(math.sqrt(3), smallAngle, math.sqrt(2), 90, 1, "#7F7F7F")
    turtle.right(mediumAngle)
    triangle(1, 90, math.sqrt(2), smallAngle, math.sqrt(3), "#7F7F7F")

    turtle.forward(size)
    turtle.left(90)

    triangle(math.sqrt(2), 45, 2, 45, math.sqrt(2), "#7F7F7F")

    turtle.forward(math.sqrt(2)*size)
    turtle.left(90)

    triangle(2, 45, math.sqrt(2), 90, math.sqrt(2), "#7F7F7F")

    turtle.right(45)

    triangle(math.sqrt(2), 90, 1, mediumAngle, math.sqrt(3), "#7F7F7F")

    turtle.forward(math.sqrt(2)*size)
    turtle.left(90)

    triangle(math.sqrt(2), smallAngle, math.sqrt(3), mediumAngle, 1, "#7F7F7F")

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

# Calculate landmarks
landmarks = [((sizeRatio/2+3)/sizeRatio, 0)]
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
gotoOnSquare(0, landmarks[0][0])
turtle.penup()

gotoOnSquare(1-landmarks[0][0], 0)
turtle.pendown()
gotoOnSquare(1, landmarks[0][0])
turtle.penup()

gotoOnSquare(landmarks[0][0], 1)
turtle.pendown()
gotoOnSquare(0, 1-landmarks[0][0])
turtle.penup()

gotoOnSquare(1-landmarks[0][0], 1)
turtle.pendown()
gotoOnSquare(1, 1-landmarks[0][0])
turtle.penup()

turtle.exitonclick()
