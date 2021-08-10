import turtle
from random import random

car = turtle.Turtle()
car.shape('turtle')


# def forward():
#     car.forward(10)


car_xy = turtle.Turtle()
car_list = []
def create_car(x, y):
    turtle.tracer(False)
    car_xy.up()
    car_xy.goto(x, y)
    car_xy.fillcolor((random(), random(), random()))
    car_list.append(car_xy)
    print(car_list)

    turtle.tracer(True)

def create_fd():
    car_l = car_list
    turtle.tracer(False)
    for i in car_l:
        i.forward(1)
    turtle.tracer(True)
    turtle.ontimer(create_fd, 10)

turtle.onscreenclick(create_car)
create_fd()
# turtle.onkeyrelease(forward, key='W')

turtle.done()