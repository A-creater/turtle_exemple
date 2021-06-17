import turtle
import  math

play = turtle.Turtle()

def test(iter, x, y):
    play.goto(x, y)
    play.fillcolor('gray')
    for i in range(iter):
        play.begin_fill()

        play.circle(50)
        # play.x = 0
        # play.y = 15
        play.end_fill()
        play.lt(90)
        play.up()
        play.fd(15)
        play.down()
        play.rt(90)


        play.fillcolor('black')
        play.begin_fill()

        play.circle(35)

        play.end_fill()


iterations = 1
lt = 360/iterations

test(iterations, 0, 0)



turtle.done()
