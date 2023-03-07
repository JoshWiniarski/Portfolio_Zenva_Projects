#A simple game where you move a turtle from the beach to the ocean.
#controls are set to WASD by default.

#lesson used only absolutes for turtle location. 
#They did not describe how to set custom window dimensions, so I got creative to make it work with any size window.
from turtle import *
from random import *


width = window_width()
height = window_height()
half_height = height//2
quarter_height = height//4
half_width = width//2
quarter_width = width//4
move_distance = quarter_width//4

#display window resolution printout
print('Display Resolution', width, height)
print('Half Resolution', width //2, height //2)
print('One Quarter', width//4, height//4)

#map setup
bgcolor('#D2691E')
speed(0)
hideturtle()
penup()
goto(quarter_width, half_height)
pendown()
color('blue')
begin_fill()
goto(half_width, half_height)
goto(half_width, -half_height)
goto(quarter_width, -half_height)
goto(quarter_width, half_height)
end_fill()
penup()
goto(-quarter_width, 0)
pendown()
shape('turtle')
color('green')
showturtle()

#player interaction definitions
def move_up():
    setheading(90)
    forward(move_distance)
    check_goal()

def move_down():
    setheading(270)
    forward(move_distance)
    check_goal()

def move_left():
    setheading(180)
    forward(move_distance)
    check_goal()

def move_right():
    setheading(0)
    forward(move_distance)
    check_goal()
    
def check_goal():
    if xcor() > quarter_width:
        hideturtle()
        penup()
        color("white")
        write("YOU WIN!")
        onkey(None, "w")
        onkey(None, "d")
        onkey(None, "s")
        onkey(None, "a")
        
        
#input control  
onkey(move_up, "w")
onkey(move_right, "d")
onkey(move_down, "s")
onkey(move_left, "a")
listen()

#keeps window open
done()