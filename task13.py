posledov = [5,44,35,20]
res = []
for i in range(len(posledov)):
    if posledov[i] % 5 == 0 and posledov[i] % 7 != 0:
        res.append(posledov[i])
print(len(res), sum(res))