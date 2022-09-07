import turtle

turtle.speed(12)

# turtle.pensize(3)
# turtle.pencolor("tomato")
# turtle.circle(45)
# turtle.penup()
# turtle.forward(90)
# turtle.pensize(3)
# turtle.pendown()
# turtle.pencolor("black")
# turtle.circle(45)
# turtle.penup()
# turtle.forward(90)
# turtle.pensize(3)
# turtle.pendown()
# turtle.pencolor("red")
# turtle.circle(45)
# turtle.setheading(90)
# turtle.pensize(3)
# turtle.pendown()
# turtle.pencolor("blue")
# turtle.circle(45)
# turtle.penup()
# turtle.left(90)
# turtle.forward(90)
# turtle.setheading(90)
# turtle.pensize(3)
# turtle.pendown()
# turtle.pencolor("green")
# turtle.circle(45)
# turtle.done()

turtle.bgcolor("black")

side = 6

colors = ['red', 'yellow', 'green', 'blue', 'purple', 'orange']

for i in range(360):
    turtle.pencolor(colors[i%side])
    turtle.forward(i*3/side+i)
    turtle.left(360/side + 1)
    turtle.width(i*side/200)

print("end")



