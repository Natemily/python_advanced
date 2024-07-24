import turtle
window = turtle.Screen()


def star(side):
    a = 0
    for i in range(12):
        a += 30
        turtle.forward(side)
        turtle.backward(side)
        turtle.setheading(a)
        
side = int(input())
star(side)
window.mainloop()