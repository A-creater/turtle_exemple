
import turtle


board = turtle.Turtle()
board.speed(0)

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
    # board.fd(fd/iterations)


def test(color, rad, x, y):
    b = rad * 0.7
    a = rad - b
    board.up()
    board.goto(x, y)
    board.down()
    board.fillcolor(color)
    board.begin_fill()
    board.circle(rad)
    board.end_fill()
    board.lt(90)
    board.up()
    board.fd(a)
    board.down()
    board.rt(90)
    board.begin_fill()
    board.circle(b)
    board.end_fill()


x = -150
y = 150
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            black_white('white', 200, x, y)
            # test('#A5A1A1', 25, x + 25, y)
            x = j * 50
        else:
            black_white('black', 200, x, y)
            test('white', 25, x + 25, y)
            x = j * 50
    y = y - 50
    x = -150


turtle.done()

