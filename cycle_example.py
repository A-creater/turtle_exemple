import  turtle

post = turtle.Turtle()


post.lt(180/2)
post.up()

iteration = 5
for j in range(2):
    for i in range(iteration+1):
        post.fd(200)
        post.lt(180)
        post.fd(200)
        post.lt(90)
        post.up()
        post.fd(200/iteration)
        post.lt(90)
        post.down()
    post.lt(90)
    post.up()
    post.fd(200/iteration)
    post.down()



#post.hideturtle()
turtle.done()