#This was a simple "game" where you press a button to inflate and pop a balloon.
#import turtle
from turtle import *

#variables
diameter = 40
pop_diameter = 100
inflate_amount = 15

#definitions
def draw_balloon ():
    color('red')
    dot(diameter)
    
def inflate_balloon ():
    global diameter
    diameter = diameter + inflate_amount
    draw_balloon()
    if diameter >= pop_diameter:
        clear()
        diameter = 40
        write('POP!')
        draw_balloon()

#code
draw_balloon()

onkey(inflate_balloon, 'w')
listen()

#keep at bottom
#prevent window from closing
done()
