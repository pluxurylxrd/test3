f = [0]*10000
for a in range(-10000,10000):
    if -2 <= a < 2:
        f[a] = a**2
    else:
        f[a] = 4
print(f[-2])