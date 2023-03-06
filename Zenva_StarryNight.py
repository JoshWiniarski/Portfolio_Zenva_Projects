#This is a simple project to populate a screen with different sized dots.
from turtle import *
from random import *

bgcolor('black')
hideturtle()
speed(0)

#get the window size as variables
width = window_width()
height = window_height()

#I have a high res ultrawide display, so my default window is huge requiring larger dots.
def draw_star(xpos, ypos):
    size = randrange(5, 40)
    penup()
    goto(xpos, ypos)
    pendown()
    dot(size, "white")

for x in range(100):
    xpos = randint(- width, width)
    ypos = randint(- height, height)
    draw_star(xpos, ypos)
#The lesson instructed to use the 'round' function with roundrange to get an integer so that the code wouldn't throw an error.
#My solution is quite a bit easier.

done()