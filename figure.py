import turtle

play = turtle.Turtle()
play.speed(0)

def test(color, rad):
    b = rad * 0.7
    a = rad - b
    if color == 'black':
        play.fillcolor(color)
        play.circle(rad)

        play.lt(90)
        play.up()
        play.fd(a)
        play.down()
        play.rt(90)
        play.begin_fill()
        play.circle(b)
        play.end_fill()
    else:
        play.circle(rad)
        play.lt(90)
        play.up()
        play.fd(a)
        play.down()
        play.rt(90)
        play.circle(b)



rad = 30
black = 'black'
white = 'white'
test(black, rad)


play.hideturtle()
turtle.done()
