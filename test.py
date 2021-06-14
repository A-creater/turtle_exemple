import turtle
import  math

play = turtle.Turtle()

def test(iter, fd, lt):
    for i in range(iter):
        play.fd(fd)
        play.lt(lt)

    play.lt(90)
    play.up()
    play.fd(20)
    play.down()
    play.rt(90)

def test1(iter, fd, lt):
    for j in range(iter):
        play.fd(fd)
        play.lt(lt)


iterations = 40
iterations1 = 27
fd = 10
lt = 360/iterations
lt1 = 360/iterations1

test(iterations, fd, lt)
test1(iterations1, fd, lt1)
turtle.done()