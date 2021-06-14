import turtle




player = turtle.Turtle()  # Создать черепаху
# player.forward(100)  # 100 шагов вперед
player.shape("turtle")
player.lt(180)
player.down()
player.fd(20)
player.rt(90)
player.fd(10)
player.rt(90)
player.fd(10)
player.lt(90)
player.fd(10)
player.rt(90)
player.fd(10)
player.lt(90)
player.fd(10)
player.rt(90)
player.fd(10)
player.lt(90)
player.fd(40)
player.rt(90)
player.fd(10)
player.rt(90)
player.fd(30)
player.lt(90)
player.fd(10)
player.lt(90)
player.fd(10)
player.rt(90)
player.fd(10)
player.lt(90)
player.fd(10)
player.rt(90)
player.fd(10)
player.rt(90)
player.fd(10)
player.lt(90)
player.fd(10)
player.rt(90)
player.fd(10)
player.lt(90)
player.fd(10)
player.rt(90)
player.fd(10)
player.lt(90)
player.fd(20)
player.rt(90)
player.fd(10)
player.lt(90)
player.fd(10)
player.rt(90)
player.fd(10)
player.lt(90)
player.fd(10)
player.rt(90)
player.fd(10)
player.rt(90)
player.fd(110)
player.lt(90)
player.fd(70)
player.lt(90)
player.fd(90)
player.lt(90)
player.fd(70)

player.rt(180)
player.up()
player.fd(20)
player.rt(90)
player.fd(60)
player.down()
player.fd(20)
player.lt(90)
player.fd(20)
player.lt(90)
player.fd(20)
player.lt(90)
player.fd(20)

player.rt(90)
player.up()
player.fd(20)
player.rt(90)
player.fd(10)
player.down()
player.fd(40)
player.lt(90)
player.fd(20)
player.lt(90)
player.fd(40)
player.lt(90)
player.fd(20)


player.hideturtle()  # спрятать черепаху
player.fillcolor('black')  # установить цвет заливки
player.fillcolor(1, 0.69, 0)  # установить цвет заливки альтернативный вариант r, g, b
player.begin_fill()  # начать заливку
# player.left(90)  # Повернуть на лево 90 градусов
# player.forward(100)  # вперед 100 шагов
# player.fd(100)  # вперед 100 шагов
# player.lt(90)  # налево 90 градусов
# player.up()  # поднять карандаш
# player.down()  # опустить карандаш
# player.rt(90)  # направо 90 градусов
player.end_fill()  # закончить заливку
turtle.done()  # задержать результат

x, y = 100, 100
player.goto(x, y)  # переместить черепаху в координаты (100, 100)
player.speed(10)  # ускорение/замедление черепахи







turtle.done()  # Задержать результат