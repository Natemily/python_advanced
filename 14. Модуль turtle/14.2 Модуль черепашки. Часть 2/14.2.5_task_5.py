import turtle
window = turtle.Screen()

turtle.shape('turtle')
turtle.pensize(10)
turtle.stamp()
turtle.penup()
def star():
    a = 0
    for i in range(12):
        turtle.setheading(a)
        turtle.forward(100)
        turtle.pendown()
        turtle.pensize(5)
        turtle.forward(15)
        turtle.penup()
        turtle.pensize(10)
        turtle.forward(15)
        turtle.stamp()
        turtle.backward(130)
        a += 360/12

star()
window.mainloop()