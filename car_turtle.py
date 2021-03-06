
import turtle
from board import board_a


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

        # board_a(-200, 200)
        # ch.draw(color, x, y)
        # board[i, j] = ch
# test('white', rad, x, y)

ch.hideturtle()
turtle.done()