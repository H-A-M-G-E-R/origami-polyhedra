# Measures taken from https://en.wikipedia.org/wiki/Disdyakis_dodecahedron and https://dmccooey.com/polyhedra/DisdyakisDodecahedron.html
# Folding is similar to that deltoidal icositetrahedron from https://johnmontroll.com/books/origami-symphony-no-5/
import math
import turtle

def triangle(l1, a1, l2, a2, l3, a3, size):
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(l1*size)
    turtle.left(180-a1)
    turtle.forward(l2*size)
    turtle.left(180-a2)
    turtle.forward(l3*size)
    turtle.left(180-a3)
    turtle.end_fill()
    turtle.penup()

landmarks = []

shortLength = 1.4500488186822163018 # 2*sqrt(3*(10-sqrt(2)))/7
mediumLength = 1.9397429472460411059 # 3*sqrt(6*(2+sqrt(2)))/7
longLength = 2.3644524131865197592 # 2*sqrt(6*(10+sqrt(2)))/7

smallAngle = math.acos(1/12+math.sqrt(2)/2)
mediumAngle = math.acos(3/4-math.sqrt(2)/8)
largeAngle = math.acos(1/6-math.sqrt(2)/12)

landmarks.append(((1-math.tan(math.pi/4-smallAngle))/2, 0)) # The first landmark is found at (0.43659893228746177, 0).

angle = math.pi/4-smallAngle # 45 degrees - small angle
x = math.cos(angle)
y = math.sin(angle)

angle += math.pi-2*largeAngle # 180 degrees - 2 * large angle
x += math.cos(angle)
y += math.sin(angle)

angle += math.pi-4*smallAngle # 180 degrees - 4 * small angle
x += math.cos(angle)
y += math.sin(angle)

angle += math.pi-2*largeAngle # 180 degrees - 2 * large angle
x += math.cos(angle)
y += math.sin(angle)

landmarks.append(((1-y/x)/2, 0)) # The second landmark is found at (0.2421953560797105, 0).

print(landmarks)

size = 50

turtle.delay(0)
turtle.speed(0)
turtle.pensize(3)
turtle.color("#000000", "#BFBFBF")
turtle.hideturtle()
turtle.penup()

# Convert radians to degrees
smallAngle = smallAngle/math.pi*180
mediumAngle = mediumAngle/math.pi*180
largeAngle = largeAngle/math.pi*180

for i in range(4):
    turtle.setheading(i*90)
    turtle.goto(0,0)
    turtle.left(45-smallAngle)

    triangle(mediumLength,largeAngle,shortLength,mediumAngle,longLength,smallAngle,size)

    turtle.forward(mediumLength*size)
    turtle.left(180-2*largeAngle)

    triangle(mediumLength,smallAngle,longLength,mediumAngle,shortLength,largeAngle,size)

    turtle.forward(mediumLength*size)
    turtle.left(180-2*smallAngle)

    triangle(mediumLength,largeAngle,shortLength,mediumAngle,longLength,smallAngle,size)

    turtle.right(smallAngle)

    triangle(longLength,mediumAngle,shortLength,largeAngle,mediumLength,smallAngle,size)

    turtle.right(smallAngle)

    triangle(mediumLength,largeAngle,shortLength,mediumAngle,longLength,smallAngle,size)

    turtle.forward(mediumLength*size)
    turtle.left(180-2*largeAngle)

    triangle(mediumLength,smallAngle,longLength,mediumAngle,shortLength,largeAngle,size)

    turtle.forward(mediumLength*size)
    if i == 0:
        squareRadius = turtle.pos()[0]
    
    turtle.goto(0,0)
    turtle.setheading(i*90+45)

    triangle(longLength,mediumAngle,shortLength,largeAngle,mediumLength,smallAngle,size)

    turtle.forward(longLength*size)
    turtle.left(180-2*mediumAngle)

    triangle(longLength,smallAngle,mediumLength,largeAngle,shortLength,mediumAngle,size)

    turtle.right(mediumAngle)

    triangle(shortLength,largeAngle,mediumLength,smallAngle,longLength,mediumAngle,size)

    turtle.forward(shortLength*size)
    turtle.left(180-2*largeAngle)

    triangle(shortLength,mediumAngle,longLength,smallAngle,mediumLength,largeAngle,size)

    turtle.forward(shortLength*size)
    turtle.left(180-2*mediumAngle)

    triangle(shortLength,largeAngle,mediumLength,smallAngle,longLength,mediumAngle,size)

    turtle.right(mediumAngle)

    triangle(longLength,smallAngle,mediumLength,largeAngle,shortLength,mediumAngle,size)

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
turtle.goto(0,0)
turtle.pendown()
turtle.goto((-1+2*landmarks[0][0])*squareRadius,(-1+2*landmarks[0][1])*squareRadius)
turtle.penup()

turtle.exitonclick()
