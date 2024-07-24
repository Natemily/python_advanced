import turtle
window = turtle.Screen()


def hexagon(side):
    for i in range(6):
        turtle.forward(side)
        turtle.left(60)
       
side = int(input())
hexagon(side)
window.mainloop()