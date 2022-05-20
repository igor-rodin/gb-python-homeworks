# Задача 1
# Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д. (-3)**(N-1)

def powers_of_three(num):
    return [(-3)**num for num in range(num)]


n = 7
print(powers_of_three(n))

# Задача 2
# Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.


def count_str(substr, string):
    idx = 0
    count = 0
    idx = string.find(substr, idx)
    while idx != -1:
        count += 1
        idx = string.find(substr, idx + len(substr))
    return count


string = "PythonIsPyt where is Pyth where is Pyth"
what = "where is"

print(
    f"Количество вхождений '{what}' in '{string}' - {count_str(what, string)}")

# Задача 3
# Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [1, 2, 6, 24] - N!


def factorials(num):
    res = [1]*num
    for i in range(1, num):
        res[i] = res[i-1]*(i+1)

    return res


num = 6
print(factorials(num))
