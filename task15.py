from math import prod
posledov = [7,3,4,5,14]
res = []
for i in range(len(posledov)):
    if posledov[i] % 7 == 0:
        res.append(posledov[i])
print(prod(res))