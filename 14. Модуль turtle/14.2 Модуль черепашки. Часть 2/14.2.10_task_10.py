from turtle import *
pensize(5)


def moving(x, y):
  penup()
  goto(x, y)
  pendown()
  
  
colors = ['chartreuse', 'red', 'black', 'deepskyblue', 'yellow']
coords = [(55, 0), (105, 60), (0, 60), (-105, 60), (-50, 0)]

for i in range(5):
  moving(*coords[i])
  color(colors[i])
  circle(50)