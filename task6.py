import math
x = float(input('Введи действительное число:'))
a = int(input('Введи номер действия (1 - возвести число в квадрат, 2 - извлечь корень квадратный, 3 - вычислить синус, 4 - косинус):'))
if a == 1:
    print(x**2)
if a == 2:
    print(x ** 1/2)
if a == 3:
    print(math.sin(x))
if a == 4:
    print(math.cos(x))