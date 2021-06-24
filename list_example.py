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
w = [i for i in range(n) if i % 2 == 0]  # Генератор с условиями
c[0] = 1  # Заменить нулевой элемент списка числом 1
del c[4]  # Удалить 4-й элемент списка
t = c + b  # Объединение списков
c.append(10)  # Добавление элемента в конец списка
bool(a)  # Есть ли элементы в списке а
len(c)  # Узнать количество элементов в списке
a = []  # Очистить список
d.clear()  # Очистить список
b = c.pop()  # Забрать последний элемент из списка и сохранить в b
a.pop()  # вынимает элемент списка сзади
position = 3
a.insert(position, 33)  # Вставить значение 33 в позицию position
a = [0, 1, 2, 1, 0, 0, 1, 0]
a = ['pawn', 'horse', 'pawn', ]

for item in a:
    print(item)

for item in a:
    if item == 'pawn':
        paint_pawn()
    elif item == 'horse':
        paint_horse()
    elif item == 'king':
        paint_king()
    else:
        paint_empty()
    print(item)