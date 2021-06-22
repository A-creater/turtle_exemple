
import turtle


board = turtle.Turtle()
# fd = 200

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


x = -50
y = 0
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            black_white('white', 200, x, y)
            x = j * 50
        else:
            black_white('black', 200, x, y)
            x = j * 50
    y = y - 50
    x = -50




def test(color, rad, x, y):
    b = rad * 0.7
    a = rad - b
    board.up()
    board.goto(x, y)
    board.down()
    board.fillcolor(color)
    board.circle(rad)
    board.lt(90)
    board.up()
    board.fd(a)
    board.down()
    board.rt(90)
    board.begin_fill()
    board.circle(b)
    board.end_fill()






# test('black', 25, 0, 0)
# test('white', 25, 0, 0)
# c = -100
# f = -50
#
# for b in range(4):
#     black_white(200, c, 0)
#     c = c + 100
    # for d in range(8):
    #     black_white(200, c, -50)
    #     # f = f + 50
# e = -75
# for g in range(8):
#     rad = 25
#     black = 'black'
#     white = 'white'
#     test(black, rad, e, 0)
#     e = e + 50






turtle.done()

