#This was a simple project which instructed me to draw several different circles at specifics size, color, and distance from one another using turtle
from turtle import *

speed(0)
bgcolor("black")
color('orange')
begin_fill()
circle(60)
end_fill()
penup()
forward(100)

color('gray')
begin_fill()
circle(20)
end_fill()
penup()
forward(80)

color('red')
begin_fill()
circle(40)
end_fill()
penup()
forward(90)

color('green')
begin_fill()
circle(30)
end_fill()


#keep at bottom
#prevent window from closing
done()