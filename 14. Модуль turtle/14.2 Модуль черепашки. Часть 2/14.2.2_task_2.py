import turtle
window = turtle.Screen()

turtle.pensize(1)
for i in range(2):
    
    turtle.forward(200)
    turtle.pensize(5)
    turtle.dot()
    turtle.pensize(1)
    turtle.left(90)
    turtle.forward(100)
    turtle.pensize(5)
    turtle.dot()
    turtle.pensize(1)
    turtle.left(90)

window.mainloop()