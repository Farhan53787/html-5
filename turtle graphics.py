import turtle

turtle.Screen().bgcolor("red")

sc = turtle.Screen()

sc.setup(600, 600)

sc.title("Turtle Graphics")
 
turtle.right(30)
turtle.forward(100)

turtle.right(120)
turtle.forward(100)

turtle.right(120)
turtle.forward(100)

turtle.penup()
turtle.goto(-200, 200)

turtle.pendown()
turtle.right(90)
turtle.forward(100)

turtle.right(90)
turtle.forward(100)

turtle.right(90)
turtle.forward(100)

turtle.right(90)
turtle.forward(100)

turtle.penup()

turtle.goto(300, 400)


turtle.done()