import turtle

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Button(turtle.Turtle):
    point1: Point
    point2: Point
    title: str

    def __init__(self, point1: Point, point2: Point, title: str):
        super(Button, self).__init__()

        self.point1 = point1
        self.point2 = point2
        self.title = title

        self.draw_button()


    def draw_button(self):
        """ Рисование кнопки"""
        turtle.tracer(False)
        self.hideturtle()
        self.up()
        self.goto(self.point1.x, self.point1.y)
        self.down()
        self.goto(self.point2.x, self.point1.y)
        self.goto(self.point2.x, self.point2.y)
        self.goto(self.point1.x, self.point2.y)
        self.goto(self.point1.x, self.point1.y)
        turtle.tracer(True)

    def on_button(self, x, y):
        """ Обработчик нажатия кнопки"""
        pass

    def test_button(self, x: int, y: int):
        """ Проверка нажатия на кнопку и вызов обработчика"""
        pass

class SquareButton(Button):
    def on_button(self, x, y):
        """ Обработчик нажатия на кнопку"""
        print('Нажата квадратная кнопка')

    def test_button(self, x: int, y: int):
        if self.point1.x < x < self.point2.x and self.point1.y > y > self.point2.y:
            print(f'( {x}, {y})')
            self.on_button(x, y)

class RoundButton(Button):
    pass


class HelloButton(SquareButton):
    def on_button(self, x, y):
        print(f'HelloButton {self.title}')
        turtle.tracer(False)
        t = turtle.Turtle()
        t.up()
        t.goto(x, y)
        turtle.tracer(True)


b1 = SquareButton(Point(-300, 0), Point(-200, -200), title="1")
b2 = SquareButton(Point(0, 0), Point(200, -200), title="2")
b4 = SquareButton(Point(-50, 40), Point(20, -20), title="3")

builtins = [b1, b2, b4]


def on_click_screen(x, y):
    for obj in builtins:
        obj.test_button(x, y)

# def button_on_click(x, y):
#     if x1 < x < x2 and y1 > y > y2:
#         print(f"Квадратная кнопка нажата {x}, {y}")
#     if (x**2+y**2) <= (radius**2):
#
#         print(f"Круглая кнопка {x}, {y}")


turtle.onscreenclick(on_click_screen)
turtle.done()



# (x - x0)^2 + (y - y0)^2 <= R^2

