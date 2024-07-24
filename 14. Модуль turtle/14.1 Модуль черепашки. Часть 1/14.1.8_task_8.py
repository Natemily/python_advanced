import turtle
window = turtle.Screen()


def hexagon(side):
    for i in range(2):
        turtle.forward(side)
        turtle.left(60)
        turtle.forward(side)
        turtle.left(120)

def flawer(side):
    a = 10
    for i in range(10):
        turtle.setheading(30+a)
        hexagon(side)
        a += 36
       
side = int(input())
flawer(side)
window.mainloop()