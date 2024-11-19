posledov = [-4,5,4,-2]
res = []
for i in range(len(posledov)):
    if posledov[i] > 0:
        res.append(posledov[i])
print(sum(res) * 2)