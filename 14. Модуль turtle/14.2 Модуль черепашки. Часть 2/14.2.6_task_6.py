import turtle
window = turtle.Screen()

turtle.shape('turtle')
turtle.pensize(10)
turtle.stamp()
turtle.penup()
def star():
    a = 0
    b = 0
    for i in range(30):
        a += 10
        turtle.forward(b)
        turtle.stamp()
        turtle.backward(b)
        turtle.setheading(a)
        
        a += 10
        b += 5



star()
window.mainloop()