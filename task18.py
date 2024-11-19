posled = [3,45,64,2,2]
res = []
for i in range(len(posled)):
    for n in range(i+1, len(posled)):
        res.append(posled[n])
print(sum(res) / len(res))
print(res)