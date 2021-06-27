import pprint

n = 9
a = [0] * n
value = 23
a[1] = value
a[3] = 12.5
a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()

cars = ['Audi', 'bmw', 'pegeote']
for i in cars:
    print(i)


count = [[0] * n] * n
# pprint.pprint(count)

for ii in range(len(count)):
    for jj in range(len(count[ii])):
        print(count([ii][jj]), end=' ')
    print()


