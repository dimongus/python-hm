# Найдите сумму цифр трехзначного числа.


# n = input('введите 3х значное число: ')
# print(int(n[0])+int(n[1])+int(n[2]))

# =========================================================

# Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, 
# что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?

# x = int(input("Сколько всего журавлей? :"))
# print((x//6), ((x//6)*4), (x//6))

# =================================================================

# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, 
# которая проверяет счастливость билета.

# n = (input(" Введите номер билета: "))

# sum1=int(n[0])+int(n[1])+int(n[2])
# sum2=int(n[3])+int(n[4])+int(n[5])
# if sum1==sum2:
#   print('Счастливый')
# else:
#   print('Обычный')

# =================================================================
#  Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

n = int(input("размер 1: "))
m = int(input("размер 2: "))
k = int(input("количество долек: "))
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('да')
else:
    print('нет')