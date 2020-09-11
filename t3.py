# make a graph win
# draw the gameboard lines
# click from players
# variable of whos turn it is
# draw an x or o in it
# see if legal move
# determin who wins
# name the quadrants


from graphics import *
board = [10,11,12,13,14,15,16,17,18]

def drawboard(wnd):
    line = Line(Point(0,200),Point(600,200))
    line.draw(wnd)
    line = Line(Point(0,400),Point(600,400))
    line.draw(wnd)
    line = Line(Point(200,0),Point(200,600))
    line.draw(wnd)
    line = Line(Point(400,0),Point(400,600))
    line.draw(wnd)



def whichsquare(pnt):
    if (0 <= pnt.x <= 200) and (0 <= pnt.y <= 200):
        return 0
    elif (200 <= pnt.x <= 400) and (0 <= pnt.y <= 200):
        return 1
    elif (400 <= pnt.x <= 600) and (0 <= pnt.y <= 200):
        return 2
    elif (0 <= pnt.x <= 200) and (200 <= pnt.y <= 400):
        return 3
    elif (200 <= pnt.x <= 400) and (200 <= pnt.y <= 400):
        return 4
    elif (400 <= pnt.x <= 600) and (200 <= pnt.y <= 400):
        return 5
    elif (0 <= pnt.x <= 200) and (400 <= pnt.y <= 600):
        return 6
    elif (200 <= pnt.x <= 400) and (400 <= pnt.y <= 600):
        return 7
    elif (400 <= pnt.x <= 600) and (400 <= pnt.y <= 600):
        return 8
    else:
        print("Error, didn't return expected value", pnt)

def winner(winningboard):
        if winningboard[0] == winningboard[1] == winningboard[2] or winningboard[3] == winningboard[4] == winningboard[5] or winningboard[6] == winningboard[7] == winningboard[8] or winningboard[0] == winningboard[3] == winningboard[6] or winningboard[1] == winningboard[4] == winningboard[7] or winningboard[2] == winningboard[5] == winningboard[8] or winningboard[0] == winningboard[4] == winningboard[8] or winningboard[2] == winningboard[4] == winningboard[6]:
            return 1

def main():
    win = GraphWin("Tic Tac Toe", 600, 600)
    win.setBackground(color_rgb(255, 255, 255))
    drawboard(win)
    player = 1
    xs =  [Text(Point(100,100), "X"),Text(Point(300,100), "X"),Text(Point(500,100), "X"),Text(Point(100,300), "X"),Text(Point(300,300), "X"),Text(Point(500,300), "X"),Text(Point(100,500), "X"),Text(Point(300,500), "X"),Text(Point(500,500), "X")]
    os = [Text(Point(100,100), "O"),Text(Point(300,100), "O"),Text(Point(500,100), "O"),Text(Point(100,300), "O"),Text(Point(300,300), "O"),Text(Point(500,300), "O"),Text(Point(100,500), "O"),Text(Point(300,500), "O"),Text(Point(500,500), "O")]
    
    while True:
        mousepos = win.getMouse()
        square = whichsquare(mousepos)
        if square == 0 and player == 1 and board[square] != 1 and board[square] != 2:
            xs[0].draw(win).setSize(36)
            os[0].undraw()
        elif square == 0 and player == 2 and board[square] != 1 and board[square] != 2:
            os[0].draw(win).setSize(36)
            xs[0].undraw()
        elif square == 1 and player == 1 and board[square] != 1 and board[square] != 2:
            xs[1].draw(win).setSize(36)
            os[1].undraw()
        elif square == 1 and player == 2 and board[square] != 1 and board[square] != 2:
            os[1].draw(win).setSize(36)
            xs[1].undraw()
        elif square == 2 and player == 1 and board[square] != 1 and board[square] != 2:
            xs[square].draw(win).setSize(36)
            os[square].undraw()
        elif square == 2 and player == 2 and board[square] != 1 and board[square] != 2:
            os[square].draw(win).setSize(36)
            xs[square].undraw()
        elif square == 3 and player == 1 and board[square] != 1 and board[square] != 2:
            xs[square].draw(win).setSize(36)
            os[square].undraw()
        elif square == 3 and player == 2 and board[square] != 1 and board[square] != 2:
            os[square].draw(win).setSize(36)
            xs[square].undraw()
        elif square == 4 and player == 1 and board[square] != 1 and board[square] != 2:
            xs[square].draw(win).setSize(36)
            os[square].undraw()
        elif square == 4 and player == 2 and board[square] != 1 and board[square] != 2:
            os[square].draw(win).setSize(36)
            xs[square].undraw()
        elif square == 5 and player == 1 and board[square] != 1 and board[square] != 2:
            xs[square].draw(win).setSize(36)
            os[square].undraw()
        elif square == 5 and player == 2 and board[square] != 1 and board[square] != 2:
            os[square].draw(win).setSize(36)
            xs[square].undraw()
        elif square == 6 and player == 1 and board[square] != 1 and board[square] != 2:
            xs[square].draw(win).setSize(36)
            os[square].undraw()
        elif square == 6 and player == 2 and board[square] != 1 and board[square] != 2:
            os[square].draw(win).setSize(36)
            xs[square].undraw()
        elif square == 7 and player == 1 and board[square] != 1 and board[square] != 2:
            xs[square].draw(win).setSize(36)
            os[square].undraw()
        elif square == 7 and player == 2 and board[square] != 1 and board[square] != 2:
            os[square].draw(win).setSize(36)
            xs[square].undraw()
        elif square == 8 and player == 1 and board[square] != 1 and board[square] != 2:
            xs[square].draw(win).setSize(36)
            os[square].undraw()
        elif square == 8 and player == 2 and board[square] != 1 and board[square] != 2:
            os[square].draw(win).setSize(36)
            xs[square].undraw()

        if board[square] is not 1 and board[square] is not 2:
            print(board[square])
            board[square] = player
            if winner(board) == 1:
                win.setBackground(color_rgb(0, 0, 0))
                if player == 1:
                    Text(Point(300,300), "X Is The WINNER!!").draw(win).setTextColor(color_rgb(255, 255, 255))
                if player == 2:
                    Text(Point(300,300), "O Is The WINNER!!").draw(win).setTextColor(color_rgb(255, 255, 255))
            if player == 1:
                player = 2
            else:
                player = 1
        print(board)
        if winner(board) == 1:
            win.setBackground(color_rgb(0, 0, 0))





        # c = Circle(mousepos), random.randint(0, 100))
        # c.setFill(color_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        # c.draw(win)
        win.getMouse()  # Pause to view result
    win.close()

main()
