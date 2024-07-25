import turtle
window = turtle.Screen()


turtle.pensize(5)
turtle.dot()
turtle.pensize(1)
def star(n):
    a = 360/n
    for i in range(n):
        turtle.forward(150)
        turtle.stamp()
        turtle.backward(150)
        turtle.setheading(a)
        a += 360/n

        
n = int(input())
star(n)
window.mainloop()