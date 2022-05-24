# Задача 1
# Найти сумму чисел списка стоящих на нечетной позиции
# Пример: [1, 2, 3, 4] -> 4
def sum_odd(list):
    sum = 0
    for i in range(0, len(list), 2):
        sum += list[i]
    return sum


list = [1, 2, 3, 4]
print("Задача 1")
print(f"Сумма чисел на нечетных позициях списка {list}: {sum_odd(list)}")
