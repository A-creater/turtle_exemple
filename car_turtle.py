
import turtle
from board import board_a

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

#
# class Car(turtle.Turtle):
#     mileage = 0
#
#     def forward(self, distance: float) -> None:
#         super().forward(distance)
#         self.mileage += distance
# car.mileage
#
# car = Car()
# car2 = Car()
# car3 = Car()
# car4 = Car()
# for i in range(60):
#     car4.forward(10*(i % 5))
#     car4.left(30)
# car2.fd(100)
# for j in range(60):
#     for f in range(60):
#         car2.fd(10)
#         car2.lt(20)
#     car2.fd(20)
#     car2.lt(10)



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
    # def draw(self):


    def draw(self, color, x, y):
        ch.board_a()


ch = Checker()

ch.create(ch.white, ch.x, ch.y)
ch.draw()
        # board_a(-200, 200)
        # ch.draw(color, x, y)
        # board[i, j] = ch
# test('white', rad, x, y)




turtle.done()