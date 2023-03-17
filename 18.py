n = int(input('Введите количество элементов: '))
count = 0
lst = list(map(int, input('Введите элементы списка через пробел: ').split()))

if len(lst) != n or n == 0:
    print('Число введенных элементов не соответствуют заявленному количеству!')
else:
    X = int(input('Введите число X: '))
    mini = abs(X - lst[0])
    index = 0
    for i in range(n):
        count = abs(X - lst[i])
        if count < mini:
            mini = count
            index = i
    print(f'Число {lst[index]} - ближайшее к числу {X}')
