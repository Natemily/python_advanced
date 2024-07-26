import turtle
window = turtle.Screen()


def triple():
    for i in range(3):
        turtle.left(120)
        turtle.forward(200)

triple()
turtle.penup()
turtle.goto(0, 120)
turtle.pendown()
turtle.setheading(60)
triple()

window.mainloop()