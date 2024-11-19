a = int(input('Введи первое число:'))
b = int(input('Введи второе число:'))
c = int(input('Введи третье число:'))
d = int(input('Введи четвертое число:'))
if a <= b <= c <= d:
    a = d
    b = d
    c = d
    print(a,b,c,d)
elif a > b > c > d:
    print(a,b,c,d)
else:
    print(a**2,b**2,c**2,d**2)
