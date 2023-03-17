# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. 
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например,
# у операции умножения.


def printTable(operation, numRows = 5, numColumns = 5):
    space = "   "
    print(space.join([str(i) for i in range(1, numColumns + 1)]))
    for i in range(2, numRows + 1):
        print(i, end = space)
        for j in range(2, numColumns + 1):
            print(operation(i, j), end = space)
        print()

printTable(lambda x, y: x * y)