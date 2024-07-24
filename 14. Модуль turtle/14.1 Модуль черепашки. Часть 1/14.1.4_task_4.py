import turtle
window = turtle.Screen()


def square(side, a):
    turtle.setheading(90+a)
    for i in range(4):
        turtle.forward(side)
        turtle.left(90)

def lotus(side, a):
    for i in range(4):
       square(side, a)
       a += 90
       
side = int(input())
lotus(side, 0)
lotus(side, 45)
window.mainloop()