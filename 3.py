# ребуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X

# a = int(input("Введите число элементов: "))
# list_1 = [i for i in range(1, a + 1)]
# print(list_1)

# n = int(input("Введите число которое нужно найти: "))
# count = 0
# for i in list_1:
#   if i == n:
#     count += 1
# print(count)


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


#  Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X


a = [int(i) for i in input('Введите кол-во элементов: ').split()]
b = int(input('Введите число: '))
number = 0
for i in range(len(a)):
    if (b - a[i]) < b - number and b - a[i] > 0:
        number = i
print(f"Ближайшее число: {a[number]}")
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++