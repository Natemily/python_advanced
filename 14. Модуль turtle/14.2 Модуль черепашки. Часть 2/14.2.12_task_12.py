import turtle as t
from random import randint
t.Screen().setup(400,400)
t.speed(0)
t.Screen().bgcolor('lightblue')
def sneg(raz,color):
  t.pencolor(color)
  for i in range(8):
    for i in range(3):
      t.forward(raz/4)
      t.right(45)
      t.forward(raz/4)
      t.backward(raz/4)
      t.left(90)
      t.forward(raz/4)
      t.backward(raz/4)
      t.right(45)
    t.forward(raz/4)
    t.backward(raz)
    t.right(45)
for i in range(8):
  t.penup()
  t.goto(randint(-200,200),randint(-200,200))
  t.pendown()
  raz=randint(3,70)
  color=(randint(1,220),randint(1,220),randint(1,220))
  sneg(raz,color)