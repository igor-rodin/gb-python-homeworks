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

# Задача 2
# Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]


def prod_pairs(list):
    size = len(list)//2 + len(list) % 2
    prod = [0]*size
    for i in range(size):
        prod[i] = (list[i]*list[-1-i])
    return prod


l1 = [2, 3, 8, 5, 6]
l2 = [2, 3, 5, 6]
print("----------------------\nЗадача 2")
print(f"Произведение пар чисел в списке {l1} -> {prod_pairs(l1)}")
print(f"Произведение пар чисел в списке {l2} -> {prod_pairs(l2)}")

# Задача 3
# В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] = > 0.19


def max_min_dif(list):
    min_frac = 1
    max_frac = 0
    for val in list:
        dot_idx = str(val).find(".")
        if dot_idx == -1:
            continue
        frac = float("0." + str(val)[dot_idx + 1:])
        min_frac = min(min_frac, frac)
        max_frac = max(max_frac, frac)
    return max_frac - min_frac


l3 = [1.1, 1.2, 3.1, 5, 10.01]
print("----------------------\nЗадача 3")
print(
    f"Разница между максимальным и минимальным значением дробной части элементов списка {l3} -> {max_min_dif(l3)}")

# Задача 4
# Написать программу преобразования десятичного числа в двоичное


def dec_to_bin(digit):  # digit - целое беззнаковое число
    bin_number = []
    while digit > 0:
        bin_number.append(str(digit % 2))
        digit //= 2
    bin_number.reverse()

    return "".join(bin_number)


number = 79
print("----------------------\nЗадача 4")
print(f"{number} -> {dec_to_bin(number)}")

# Экстра-задачи:
# 1. Написать программу преобразования двоичного числа в десятичное.


def bin_to_dec(bin_num: str) -> int:  # предполагаем число bin_num беззнаковым
    dec_num = 0
    for i in range(len(bin_num)):
        dec_num += int(bin_num[-1-i]) * (2**i)
    return dec_num


number = "1001111"
print("----------------------\nExtra_1")
print(f"Bin: {number} -> decimal number: {bin_to_dec(number)}")
