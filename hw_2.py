import math
import random
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

# 3.Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих. Начиная с 1 и 2, первые 10 элементов будут:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.


def sum_even_fib():
    max_fib = 4_000_000
    fib_1 = 1
    fib_2 = 2
    sum = fib_2
    fib = fib_1 + fib_2
    while fib <= max_fib:
        if fib % 2 == 0:
            sum += fib
        fib_1, fib_2 = fib_2, fib
        fib = fib_1 + fib_2
    return sum


print("----------------------\nExtra_3")
print(
    f"Сумма всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона: {sum_even_fib()}")

# 2. Создайте программу, которая будет играть в игру “коровы и быки” с пользователем. Игра работает так:

# Случайным образом генерируйте 4-значное число. Попросите пользователя угадать 4-значное число.
# За каждую цифру, которую пользователь правильно угадал в нужном месте, у них есть “корова”.
# За каждую цифру, которую пользователь угадал правильно, в неправильном месте стоит “бык”.
# Каждый раз, когда пользователь делает предположение, скажите им, сколько у них “коров” и “быков”.
# Как только пользователь угадает правильное число, игра окончена. Следите за количеством догадок,
# которые пользователь делает на протяжении всей игры, и сообщите пользователю в конце.


def num_to_list(num):
    num_list = []
    while num > 0:
        num_list.append(num % 10)
        num //= 10
    num_list.reverse()
    return num_list


def count_cows_bulls(number_rnd: list, number_guess: list):
    cows = 0
    bulls = 0
    for i in range(len(number_rnd)-1, -1, -1):
        if (number_rnd[i] == number_guess[i]):
            cows += 1
            number_rnd.remove(number_rnd[i])
            number_guess.remove(number_guess[i])

    for i in range(len(number_rnd)-1, -1, -1):
        if (number_rnd[i] in number_guess):
            bulls += 1
            number_guess.remove(number_rnd[i])
            number_rnd.remove(number_rnd[i])

    return (cows, bulls)


def cows_and_bulls():
    rnd = random.randrange(1000, 10000)
    print(f"Подсказка - сгенерированное число: {rnd}")
    game_over = False
    tries = 0
    bulls = 0
    cows = 0
    while not game_over:
        tries += 1
        list_rnd = num_to_list(rnd)
        print(f"У вас  коров: {cows}, быков: {bulls}")
        guess = int(input("Угадайте четырехзначное число: "))
        while guess < 1000 or guess >= 10000:
            print(f"Число должно быть четырехзначным")
            guess = int(input("Угадайте четырехзначное число: "))
        list_guess = num_to_list(guess)
        cows, bulls = count_cows_bulls(list_rnd, list_guess)

        if cows == 4:
            game_over = True

    print(
        f"Вы угадали число {rnd} c {tries} попытки. У вас  коров: {cows}, быков: {bulls}")


print("----------------------\nExtra_2")
print("Игра 'коровы' и 'быки'")
cows_and_bulls()

# 4. Простые делители числа 13195 - это 5, 7, 13 и 29.
# Каков самый большой делитель числа 600851475143, являющийся простым числом?


def primes(n):
    seads = [True]*(n + 1)
    seads[0] = seads[1] = False
    for i in range(2, math.ceil(math.sqrt(n))):
        if seads[i]:
            for j in range(i**2, n + 1, i):
                seads[j] = False
    primes = [i for i in range(2, len(seads)) if seads[i]]

    return primes


def greatest_factor(n, count_of_primes):
    big_number = n
    primes_numbers = primes(count_of_primes)
    factor = []
    product = 1
    for val in primes_numbers:
        while n % val == 0:
            factor.append(val)
            product *= val
            n //= val
        if n <= 0:
            break
    if product != big_number:
        print(
            f"Не достоточный диапазон простых чисел для нахождения общего делителя числа {big_number}")
    return factor[-1]


n = 600851475143
count_of_primes = 10000
print("----------------------\nExtra_4")
print(
    f"Наибольший простой делитель числа {n}: {greatest_factor(n, count_of_primes)}")
