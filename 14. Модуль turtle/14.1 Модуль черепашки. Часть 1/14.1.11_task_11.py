import turtle
window = turtle.Screen()


def square(side):
    for i in range(4):
        turtle.backward(side)
        turtle.right(90)

def square_lot(side):
    for i in range(30):
        square(side)
        side += 5

        
side = int(input())
square_lot(side)
window.mainloop()