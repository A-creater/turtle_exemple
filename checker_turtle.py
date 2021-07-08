import turtle
from board import board_a


class Checker(turtle.Turtle):
    black = 'black'
    white = 'white'
    x = 0
    y = 0

    def create(self, color, x, y):
        ch.goto(x, y)
        rad = 20
        b = rad * 0.7
        a = rad - b
        ch.up()

        ch.down()
        ch.fillcolor('white')
        ch.begin_fill()
        ch.circle(rad)
        ch.end_fill()
        ch.lt(90)
        ch.up()
        ch.fd(a)
        ch.down()
        ch.rt(90)
        ch.fillcolor(color)
        ch.begin_fill()
        ch.circle(b)
        ch.end_fill()

    def draw(self, x, y):
        ch.x = x
        ch.y = y
        start = ch.x
        board_a()
        for i in range(8):
            for j in range(8):
                condition = i < 3
                black_condition = i >= 5
                if (i + j) % 2 == 0:
                    ch.x += 50
                else:
                    if condition and (i + j) % 2 != 0:
                        ch.create(ch.white, ch.x, ch.y)
                        ch.up()
                        ch.x += 50
                    if black_condition and (i + j) % 2 != 0:
                        ch.create(ch.black, ch.x, ch.y)
                        ch.up()
                        ch.x += 50
            ch.y -= 50
            ch.x = start


ch = Checker()
ch.speed(0)
ch.draw((-200 + 25), (200 + 5))


turtle.done()
