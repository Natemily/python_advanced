import turtle
window = turtle.Screen()


def hexagon(side):
    for i in range(2):
        turtle.forward(side)
        turtle.left(120)
        turtle.forward(side)
        turtle.left(60)
       
side = int(input())
hexagon(side)
window.mainloop()