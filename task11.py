a = int(input('Введи целое число a:'))
b = int(input('Введи целое число b:'))
z = float(input('Введи действительное число z:'))
x = a % b
if a % b == 0:
    z = z * x
    print(z)
else:
    z = z/x
    print(z)