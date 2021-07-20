import turtle
turtle.tracer(0)

class Car(turtle.Turtle):
    def __init__(self, x, y, color, shape='triangle'):
        super().__init__(shape=shape)
        self.color(color)
        self.up()
        self.goto(x, y)
        self.down()


def attack(enemys, f, to, angle, distance):
    for enemy in enemys[f:to]:
        enemy.left(angle)
        enemy.fd(distance)


cars = []
for i in range(30):
    for j in range(30):
        car = Car(x=i * 20 - 300, y=j * 20 - 300, color='red')
        cars.append(car)


attack(cars, 0, 300, 45, 100)
attack(cars, 300, 500, -45, 30)
attack(cars, 600, len(cars), -90, 80)

c = cars[387]
c.color('green')

turtle.tracer(1)
turtle.done()
