import turtle
window = turtle.Screen()

turtle.pensize(7)
for i in range(11):
    turtle.penup()
    turtle.forward(20)
    turtle.dot()

window.mainloop()