import  turtle

post = turtle.Turtle()

def paint_figure(x, y):
    """
    нарисуем фигуру в нужном месте
    :return:
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
    for j in range(iteration):
        for i in range(iteration+1):
            post.fd(200/iteration)
            post.lt(360/iteration)
        post.fd(200/iteration)


paint_figure(100, 100)
paint_figure(100, -100)
paint_figure(-100, 100)
paint_figure(-100, -100)
paint_figure(0, 0)

#post.hideturtle()
turtle.done()