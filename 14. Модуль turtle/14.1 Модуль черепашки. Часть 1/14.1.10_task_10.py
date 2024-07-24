import turtle
window = turtle.Screen()


def star(side):
    turtle.setheading(144)
    for i in range(5):
        turtle.forward(side)
        turtle.right(144)
        
side = int(input())
star(side)
window.mainloop()