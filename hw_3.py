# 1. Найти НОК двух чисел
# lcm(a, b) = (a * b)/gcd(a, b)

import math


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
