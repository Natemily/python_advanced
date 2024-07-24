import turtle
window = turtle.Screen()

def triangle(side):
    turtle.forward(side)
    turtle.left(120)

    turtle.forward(side)
    turtle.left(120)

    turtle.forward(side)

side = int(input())
triangle(side)
window.mainloop()