import turtle
import  math

play = turtle.Turtle()


def test(iter, iter1, fd, lt):
    for i in range(iter):
        play.fd(fd)
        play.lt(lt)
    play.lt(90)
    play.up()
    play.fd(20)
    play.down()
    play.rt(90)

    for j in range(iter1):
        play.fd(fd)
        play.lt(lt1)


iterations = 40
iterations1 = 27
fd = 10
lt = 360/iterations
lt1 = 360/iterations1

test(iterations, iterations1, fd, lt)


turtle.done()
