import  turtle

post = turtle.Turtle()



# post.lt(90)
# post.up()
# post.fd(200/2)
# post.lt(90)
# post.down()
# post.fd(200/2)
# post.lt(180)
#
# iteration = 20
# for j in range(2):
#     for i in range(iteration+1):
#         post.fd(200)
#         post.lt(180)
#         post.fd(200)
#         post.lt(90)
#         post.up()
#         post.fd(200/iteration)
#         post.lt(90)
#         post.down()
#     post.lt(90)

def paint_figure(x, y, color):
    """

    :param x: координата х фигуры
    :param y: координата у фигуры
    :param color: цвет фигуры
    :return: в нужном положении рисует фигуру
    """
    post.speed(0)

    post.up()
    post.goto(x, y)
    post.down()


# post.lt(90)
# post.up()
# post.fd(200/2)
# post.lt(90)
# post.down()
# post.fd(200/2)
# post.lt(180)

# iteration = 10
# for j in range(2):
#     for i in range(iteration+1):
#         post.fd(200)
#         post.lt(180)
#         post.fd(200)
#         post.lt(90)
#         post.up()
#         post.fd(200/iteration)
#         post.lt(90)
#         post.down()
#     post.lt(90)
#     post.up()
#     post.fd(200/iteration)
#     post.down()


    iteration = 10
    for q in range(1):

        for j in range(iteration):
            post.end_fill()
            post.begin_fill()
            post.fillcolor(color)
            for i in range(iteration+1):
                post.fd(200/iteration)
                post.lt(360/iteration)

            post.fd(200/iteration)




paint_figure(100, 100, color='red')
paint_figure(100, -100, 'orange')
paint_figure(-100, 100, (1, 1, .5))
paint_figure(-100, -100, 'green')
paint_figure(0, 0, 'white')


#post.hideturtle()
turtle.done()