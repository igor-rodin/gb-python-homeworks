from __future__ import with_statement
import numbers
import random
# Задача 1:  Дан список чисел. Создать список, в который попадают числа, описывающие возрастающую последовательность.
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.
# Порядок элементов менять нельзя


def get_asc_seq(array: list) -> list:
    start_index = 0
    while True:
        asc_seq = [array[start_index]]
        for i in range(start_index + 1, len(array)):
            if array[i] > asc_seq[-1]:
                asc_seq.append(array[i])
        start_index += 1
        if len(asc_seq) > 1:
            break
    return asc_seq


array = [1, 5, 2, 3, 4, 6, 1, 7]
print("-------------------------\nЗадача 1")
print(get_asc_seq(array))

# Задача 2: Создать и заполнить файл случайными целыми значениями.
# Выполнить сортировку содержимого файла по возрастанию.


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
    write_numbers(file_name, sorted(numbers))


file_name = 'data.txt'
numbers = gen_random_seq(40, -90, 90)
write_and_sort(file_name, numbers)
