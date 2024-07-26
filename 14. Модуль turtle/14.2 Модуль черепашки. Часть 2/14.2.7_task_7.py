import turtle
window = turtle.Screen()


colors=['red', 'blue', 'yellow', 'green', 'purple', 'orange']*5
def star():
    a = 1
    len = 5
    for i in range(30):    
        turtle.pensize(a)
        turtle.pencolor(colors[i])
        turtle.forward(len)
        turtle.left(45)
        a += 1
        len += 5

star()
window.mainloop()