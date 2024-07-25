import turtle
window = turtle.Screen()

turtle.shape('turtle')
turtle.pensize(10)
turtle.stamp()
turtle.penup()
def star():
    a = 0
    for i in range(10):
        turtle.setheading(a)
        turtle.forward(50)
        turtle.stamp()
        turtle.backward(50)
        a += 360/10

star()
window.mainloop()