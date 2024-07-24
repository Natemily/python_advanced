import turtle
window = turtle.Screen()


def square():
    a = 5
    turtle.setheading(270)
    for i in range(37):
        turtle.backward(a)
        turtle.left(90)
        a += 5
       
square()
window.mainloop()