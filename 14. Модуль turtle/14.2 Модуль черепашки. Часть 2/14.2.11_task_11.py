from turtle import *
def s(x): 
  down()
  circle(x)
  up()
  
Screen().setup(500, 500), speed(10), pensize(1.2) 
s(15), rt(90), down(), fd(90), up()  
goto(-88, -44), s(88 )
goto(-150, 17), s (150) 
goto(-90, 40), begin_fill(), s(15), end_fill() 
goto(60, 40), begin_fill(), s(15), end_fill() 
goto(-175, 150), s (40) 
goto(95, 150), s (40)