from graphics import *
import random

def main():
    win = GraphWin("My Circle", 500, 500)
    win.setBackground(color_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    mousepos = win.getMouse()
    c = Circle(Point(mousepos.x,mousepos.y), random.randint(0, 100))
    c.setFill(color_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    c.draw(win)
    win.getMouse() # Pause to view result
    
main()

# 1 order book, 2 python rand int done
# make window 500 x 500 - done
# get mouse position first, draw circle on mouse position, draw in random color.
# git it to connect to git


# QUESTION: how do I know I can use x or y? It was just a guess.