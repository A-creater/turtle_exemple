import turtle


class Car(turtle.Turtle):
    mileage = 0

    def forward(self, distance: float) -> None:
        super().forward(distance)
        self.mileage += distance


car = Car()
car2 = Car()
car3 = Car()
car4 = Car()
for i in range(60):
    # car4.forward(10*(i % 5))
    # car4.left(30)





class Checker(turtle.Turtle):
    color = ''
    x = 0
    y = 0
    def create(selfself, color, x, y):
        pass
    def draw(self):
        pass

    def draw(self, color, x, y):
        pass

   ch = Checer()
    ch.draw(color, x, y)
    board[i, j] = ch

turtle.done()