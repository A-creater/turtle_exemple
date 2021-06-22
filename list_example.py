import  turtle
from math import sqrt

a = []  # Пустой список
b = [1, 2, 3, ]  # Инициализация массива
c = [0, ] * 8  # Инициализация массива из 8 элементов
field_range = 6
d = [0] * field_range # Не забываем про переменные
n = 6
e = [[0 for i in range(n)]] * n  # Список списков n раз
f = [[0] * n for i in range(n)]  # Список списков n раз
g = [[0] * n] * n  # Список списков n раз
s = [0 for i in range(n)]  # Список заполненный нулями
q = [i for i in range(n)]  # Список значений от 0 до n
u = [i*i for i in range(n)]
y = [i*i+10 for i in range(n)]
r = [i**i for i in range(n)]  # Заполнить степенью i
s = [sqrt(i) for i in range(n)]  # Корень числа
w = [i for i in range(n) if i % 2 == 0]  #  Генератор с условиями