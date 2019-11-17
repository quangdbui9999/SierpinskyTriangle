# Name: Quang Bui

import turtle
import math

def jump(x, y) :
    turtle.penup ()
    turtle.setpos(x, y)
    turtle.pendown()

def triangle(x, y, side) :
    jump(x - (side / 2), y + (side / 2))
    turtle.color("black", "cyan")
    turtle.begin_fill()
    for i in range (0, 3) :
        turtle.forward(side)
        turtle.right(120)
    turtle.end_fill()

def border(x, y, side) :
    jump(x - (side / 2), y + (side / 2))
    turtle.color("black", "red")
    turtle.begin_fill()
    for i in range (0, 3) :
        turtle.forward(side)
        turtle.left(120)
    turtle.end_fill()

def sierpinski(x, y, s) :
    if s > 10 :
        triangle(x, y, s)
        newSide = s / 2
        sierpinski(x - newSide, y - newSide / 2.6, newSide)
        sierpinski(x + newSide, y - newSide / 2.6, newSide)
        sierpinski(x + (s / 4) - (newSide/2), y + ((s * math.sqrt(3)) / 4) + (newSide/2), newSide)
      
border(0,-138,200)
sierpinski(0, 0, 100)