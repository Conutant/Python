from graphics import *

def main():
    win = GraphWin("My Circle", 100, 100)
    win.setBackground("blue")
    c = Circle(Point(50,50), 10)
    c.setFill("red")
    c.draw(win)
    print(win.getMouse()) # Pause to view result
    win.close()    # Close window when done

main()

# 1 order book, 2 python rand int
# make window 500 x 500 
# get mouse position first, draw circle on mouse position, draw in random color.
# git it to connect to git