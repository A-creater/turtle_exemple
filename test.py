import turtle
import  math

play = turtle.Turtle()

def test(iter, iter1, fd, lt, color):
    for i in range(iter):
        play.fd(fd)
        play.lt(lt)

    play.lt(90)
    play.up()
    play.fd(20)
    play.down()
    play.rt(90)
    play.fillcolor('black')
    play.begin_fill()
    for j in range(iter1):
        play.fd(fd)
        play.lt(lt1)
        play.end_fill()


iterations = 40
iterations1 = 27
fd = 10
lt = 360/iterations
lt1 = 360/iterations1


test(iterations, iterations1, fd, lt, 'black')


turtle.done()
