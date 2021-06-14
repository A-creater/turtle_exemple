import turtle
import math


play = turtle.Turtle()

d = 100
c = 3.14*d

def checker():

    for i in range(36):
        play.fd(10)
        play.lt(10)

    play.lt(90)
    play.up()
    play.fd(12)
    play.down()
    play.rt(90)

    for j in range(30):
        play.fd(10)
        play.lt(13)


checker()

turtle.done()
