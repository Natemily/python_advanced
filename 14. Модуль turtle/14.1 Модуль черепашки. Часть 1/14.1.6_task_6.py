import turtle
window = turtle.Screen()


def hexagon(side):
    for i in range(7):
        turtle.forward(side)
        turtle.left(60)

def bee(side):
    a = 0
    for i in range(6):
        turtle.setheading(180+a)
        hexagon(side)
        a -= 60
       
side = int(input())
bee(side)
window.mainloop()