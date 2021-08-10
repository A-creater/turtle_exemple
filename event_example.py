import turtle
import datetime


hour = turtle.Turtle()
minutes = turtle.Turtle()
seconds = turtle.Turtle()
hour_circle = turtle.Turtle()
hour_shtrih = turtle.Turtle()

minutes.color('red')
hour.color('blue')


hour_circle.pensize(3)
hour_circle.up()
hour_circle.goto(0, -100)
hour_circle.down()
hour_circle.circle(100)


def hour_c():
    hour_shtrih.pensize(3)
    for i in range(13):
        hour_shtrih.up()
        hour_shtrih.goto(0, 0)

        hour_shtrih.forward(80)
        hour_shtrih.down()
        hour_shtrih.forward(20)
        hour_shtrih.rt(360 / 12)




def hour_x():
    hour_shtrih.pensize(1)
    for i in range(61):
        hour_shtrih.up()
        hour_shtrih.goto(0, 0)

        hour_shtrih.forward(90)
        hour_shtrih.down()
        hour_shtrih.forward(10)
        hour_shtrih.rt(360 / 60)


hour_c()
hour_x()


def run_forward():
    seconds.goto(0, 0)
    minutes.goto(0, 0)
    hour.goto(0, 0)


    turtle.tracer(False)
    seconds.clear()
    minutes.clear()
    hour.clear()

    seconds.pensize(2)
    seconds.forward(95)
    minutes.pensize(3)
    minutes.forward(80)
    hour.pensize(5)
    hour.forward(60)

    seconds.rt(360/60)
    minutes.rt((360 / 60) / 60)
    hour.rt(((360 / 60) / 60) / 12)

    turtle.ontimer(run_forward, 1000)
    turtle.tracer(True)



# ho = turtle.numinput('', 'Введи часы')
# min = turtle.numinput('', 'Введи минуты')
t = datetime.datetime.now()
seconds.lt(90)
minutes.lt(90)
minutes.rt(360 / 60 * t.minute)
hour.lt(90)
hour.rt(360 / 12 * t.hour)
hour.rt((360 / 12) / 60 * t.hour)



turtle.ontimer(run_forward, 2000)

hour_shtrih.hideturtle()
hour_circle.hideturtle()
seconds.hideturtle()
hour.hideturtle()
minutes.hideturtle()
turtle.done()
