import math
import turtle

def triangle(l1, a1, l2, color=None):
    if color != None:
        turtle.fillcolor(color)
    prev_pos = turtle.pos()
    prev_dir = turtle.heading()

    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(l1*size)
    turtle.right(180-a1)
    turtle.forward(l2*size)

    turtle.goto(prev_pos)
    turtle.setheading(prev_dir)

    turtle.end_fill()
    turtle.penup()

def gotoOnSquare(x, y):
    turtle.goto((-1+2*x)*squareRadius,(-1+2*y)*squareRadius)

sizeRatio = math.sqrt(3)/6
squareRadius = 400
size = squareRadius*2*sizeRatio

# Setup turtle
turtle.delay(0)
turtle.speed(0)
turtle.pensize(3)
turtle.color("#000000", "#BFBFBF")
turtle.hideturtle()
turtle.penup()

# Draw net
def triangle_group():
    for _ in range(2):
        triangle(1, 60, (2-math.sqrt(2))/2)
        turtle.forward(1*size)
        turtle.right(180-60)
        turtle.forward((2-math.sqrt(2))/2*size)
        turtle.right(180)
        triangle((2-math.sqrt(2))/2, 60, 1)
        turtle.forward((2-math.sqrt(2))/2*size)
        turtle.right(180-60)
        turtle.forward(1*size)
        turtle.right(180-60)

gotoOnSquare(1/4, 0)
turtle.setheading(150)
triangle_group()
turtle.right(60)
triangle_group()

gotoOnSquare(3/4, 0)
turtle.setheading(150)
triangle_group()
turtle.right(60)
triangle_group()

gotoOnSquare(1/4, 1)
turtle.setheading(270)
triangle_group()
turtle.left(60)
triangle_group()

gotoOnSquare(3/4, 1)
turtle.setheading(270)
triangle_group()
turtle.left(60)
triangle_group()

# Draw square
turtle.setheading(0)
turtle.goto(-squareRadius,squareRadius)

turtle.pendown()
for i in range(4):
    turtle.forward(2*squareRadius)
    turtle.right(90)
turtle.penup()

# Calculate landmarks
landmarks = [(0, math.sqrt(3)/3/4*(4-math.sqrt(2))/2), (0, math.sqrt(3)/3/4*(2+math.sqrt(2))/2)]
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

gotoOnSquare(0, landmarks[0][1])
turtle.pendown()
gotoOnSquare(1, landmarks[0][1])
turtle.penup()

gotoOnSquare(0, landmarks[1][1])
turtle.pendown()
gotoOnSquare(1, landmarks[1][1])
turtle.penup()

turtle.exitonclick()
