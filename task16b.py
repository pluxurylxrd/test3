f = [0] * 10000
for a in range(-10000,10000):
    if a <= 2:
        f[a] = a**2 + 4*a + 5
    else:
        f[a] = 1 / (a**2 + 4*a + 5)
print(f[3])