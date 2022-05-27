import math
# 1. Найти НОК двух чисел
# lcm(a, b) = (a * b)/gcd(a, b)


def gcd(a, b):
    if a < b:
        return gcd(b, a)
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return int((a * b) / gcd(a, b))


# a =1071
# b = 462
a = 16
b = 20
print("-------------------------\nЗадача 1")
print(f"НОК({a},{b}) = {lcm(a, b)}")

# 2 Вычислить число pi c заданной точностью d
# Пример: при d = 0.001,  c= 3.141.
# Для вычисления используется ряд Лейбница pi/4 = Sum((-1)**n/(2 * n + 1), n = 0..inf)


def calc_pi(epsilon):
    n = 2
    pi = 4*[1, -1/3]
    dif = 1
    while dif > epsilon:
        pi.append(4*(-1)**n/(2 * n + 1))
        dif = abs(sum(pi[:-2]) - sum(pi[:-1]))
        n += 1

    str_eps = str(epsilon)
    round_val = len(str_eps[str_eps.find('.')+1:])
    return round(sum(pi), round_val)


d = 0.001
print("-------------------------\nЗадача 2")
print("Первый вариант")
print(f"Число pi(с точностью {d}) = {calc_pi(d)}")

# Вариант просто округления числа с нужной точность


def calc(number, epsilon):
    str_eps = str(epsilon)
    round_val = len(str_eps[str_eps.find('.')+1:])
    return round(number, round_val)


print("Второй вариант")
number = 3.141093153121447
print(f"Число {number}(с точностью {d}) = {calc(number, d)}")

# 3 Составить список простых множителей натурального числа N


def primes(n):
    seads = [True]*(n + 1)
    seads[0] = seads[1] = False
    for i in range(2, math.ceil(math.sqrt(n))):
        if seads[i]:
            for j in range(i**2, n + 1, i):
                seads[j] = False
    primes = [i for i in range(2, len(seads)) if seads[i]]

    return primes


def factorize(n):
    primes_numbers = primes(n)
    factors = []
    for val in primes_numbers:
        while n % val == 0:
            if val not in factors:
                factors.append(val)
            n //= val
        if n <= 0:
            break

    return factors


N = 130
print("-------------------------\nЗадача 3")
print(f"Простые множители числа {N}: {factorize(N)}")

# 4 Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]


def get_uniq(arr):
    list_uniq = []
    for val in arr:
        if val not in list_uniq:
            list_uniq.append(val)

    return list_uniq


print("-------------------------\nЗадача 4")
arr = [1, 2, 3, 5, 1, 5, 3, 10]
print(f"Неповторояющиеся элементы списка {arr} -> {get_uniq(arr)}")

# Через приведение к множеству


def get_uniq_2(arr):
    return list(set(arr))


print(f"Неповторояющиеся элементы списка {arr} -> {get_uniq_2(arr)}")

# Экстра-задачи:

# 4 . Сумма квадратов первых десяти натуральных чисел равна
# 1^2 + 2^2 + ... + 10^2 = 385
# Квадрат суммы первых десяти натуральных чисел равен
# (1 + 2 + ... + 10)^2 = 552 = 3025
# Следовательно, разность между суммой квадратов и квадратом суммы первых десяти натуральных чисел составляет 3025 − 385 = 2640.
# Найдите разность между суммой квадратов и квадратом суммы первых ста натуральных чисел.
# S_n = n*(n+1)/2- сумма первых n натуральных чисел, S_n2 = n*(n+1)*(2 * n +1)/6 - сумма квадратов первых n натуральных чисел


def std(n):
    sum_n = n*(n+1)//2
    sum_n2 = n*(n+1)*(2*n + 1)//6

    return sum_n**2 - sum_n2


print("-------------------------\nExtra задача 4")
N = 100
print(
    f"Разность между квадратом суммы и суммой квадратов первых {N} натуральных чисел = {std(N)}")
