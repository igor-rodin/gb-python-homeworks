import random
# Задача 1:  Дан список чисел. Создать список, в который попадают числа, описывающие возрастающую последовательность.
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.
# Порядок элементов менять нельзя


# Задача 1: Создать и заполнить файл случайными целыми значениями.
# Выполнить сортировку содержимого файла по возрастанию.
def select_sort(array: list) -> list:
    for i in range(len(array)):
        min_i = i
        for j in range(i+1, len(array)):
            if array[j] < array[min_i]:
                array[min_i], array[j] = array[j], array[min_i]


def gen_random_seq(list_size: int, min_val: int, max_val: int) -> int:
    return [random.randint(min_val, max_val) for _ in range(list_size)]


def write_numbers(file_name: str, data: list):
    numbers = " ".join(list(map(str, data)))
    with open(file_name, 'w') as fdata:
        fdata.write(numbers)


def read_numbers(file_name: str) -> list:
    with open(file_name, 'r') as fdata:
        numbers = list(map(int, fdata.read().split()))
    return numbers


def write_and_sort(file_name, data):
    write_numbers(file_name, data)
    numbers = read_numbers(file_name)
    select_sort(numbers)
    write_numbers(file_name, numbers)


file_name = 'data.txt'
numbers = gen_random_seq(30, -90, 90)
write_and_sort(file_name, numbers)

# Задача 2: Дан список чисел. Создать список в который попадают числа,
# описывающие возрастающую последовательность и содержащие максимальное количество элементов. 
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
# [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7]
# Порядок элементов менять нельзя


def lis(array: list) -> list:
    larg_length = [0]*(len(array))
    for i in range(len(array)):
        for j in range(i):
            if array[j] < array[i] and larg_length[j] > larg_length[i]:
                larg_length[i] = larg_length[j]
        larg_length[i] += 1

    result = []
    max_length = max(larg_length)
    idx_max_length = larg_length.index(max_length)
    result.append(array[idx_max_length])
    while idx_max_length >= 0:
        if max_length - larg_length[idx_max_length-1] == 1:
            result.append(array[idx_max_length-1])
            max_length = larg_length[idx_max_length-1]
        idx_max_length -= 1

    return sorted(result)


# ar = [1, 5, 2, 3, 4, 6, 1, 7, 2]
ar = [5, 2, 3, 4, 6, 1, 7]
print("-------------------------\nЗадача 2")
print(f"{ar} -> {lis(ar)}")
# Экстра-задачи:

# Задача 1: Пирамида пивных банок будет квадратировать количество банок на каждом уровне - 1 банка на верхнем уровне,
# 4 на втором, 9 на следующем, 16, 25...
# Определите функцию beeramid, чтобы вернуть количество полных уровней пирамиды пивных банок,
# которую вы можете сделать, учитывая параметры: реферальный бонус и цена пивной банки.
# Например:
# beeramid(1500, 2)  # 12
# beeramid(5000, 3)  # 16


def sum_of_squares(n):
    return n * (n + 1) * (2 * n + 1)//6


def beeramid(bonus: int, beer_price: int):
    level = 1
    beer_counts = bonus // beer_price
    while sum_of_squares(level) < beer_counts:
        level += 1

    return level - 1


bonus = 5000
price = 3
print("-------------------------\nExtra задача 1")
print(f"Количество полных уровней: {beeramid(bonus, price)}")
