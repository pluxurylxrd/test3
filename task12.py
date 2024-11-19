posledov = [1,4,2,4,5] # Какая-то последовательность
for i in range(len(posledov)):
    for j in range(i+1,len(posledov) - 1):
        print(posledov[i],posledov[j])