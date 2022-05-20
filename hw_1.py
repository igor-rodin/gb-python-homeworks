# Задача 1
# Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д. (-3)**(N-1)

def powers_of_three(num):
    return [(-3)**num for num in range(num)]


n = 5
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


string = "PythonIsPyt where Pyth wherePyth"
what = "where"

print(
    f"Количество вхождений '{what}' in '{string}' - {count_str(what, string)}")
