
current_number = input('Текущее число:')
while True:
    next_number = input('Следующее число:')
    if next_number < current_number:
        print('Стоп')
        break
    current_number = next_number


