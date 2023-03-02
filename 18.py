a = [int(i) for i in input('Введите кол-во элементов: ').split()]
b = int(input('Введите число: '))
number = 0
for i in range(len(a)):
    if (b - a[i]) < b - number and b - a[i] > 0:
        number = i
print(f"Ближайшее число: {a[number]}")