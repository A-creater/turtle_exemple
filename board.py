
import turtle


board = turtle.Turtle()

board.speed(0)
# if __name__ == '__main__':
def black_white(color, fd, x, y):  # Рисует
    board.up()
    board.goto(x, y)
    board.down()
    iterations = 4
    board.fillcolor(color)
    board.begin_fill()
    for i in range(iterations):
        board.fd(fd/iterations)
        board.lt(360/iterations)
    board.end_fill()
    board.fd(fd/iterations)



def board_a():
    x = -200
    y = 200
    start = x
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                black_white('white', 200, x, y)
                x += 50
                j *= 50
            else:
                black_white('black', 200, x, y)
                x += 50
                j *= 50
        y = y - 50
        x = start




