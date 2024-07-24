import turtle
window = turtle.Screen()


def square(side, a):
    turtle.setheading(7+a)
    for i in range(4):
        turtle.forward(side)
        turtle.left(90)

def lotus(side):
    a = 8
    for i in range(3):
       square(side, a)
       a += 30
       

side = int(input())
lotus(side)
window.mainloop()