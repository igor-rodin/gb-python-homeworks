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
