def equation(a,b,c):
    if a == 0:
        return False
    print(f'{a}x^2 + {b}x + {c} = 0:')
    discr = b**2 - 4*a*c
    if discr > 0:
        x1 = (-b + (discr ** 1/2)) / (2*a)
        x2 = (-b - (discr ** 1/2)) / (2*a)
        print(f'x1= {x1}, x2 = {x2}')
    elif discr == 0:
        x = -b / (2*a)
        print(f'x = {x}')
    else:
        return False
print(equation(1,4,4))
