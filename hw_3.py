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
        dif = abs(sum(pi[:-1]) - sum(pi[:-2]))
        n += 1

    return math.floor(sum(pi)*int(1/epsilon))*epsilon


d = 0.001
print("-------------------------\nЗадача 2")
print(f"Число pi(с точностью {d}) = {calc_pi(d)}")


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

# Через приведение к множеству


def get_uniq_2(arr):
    return list(set(arr))


print("-------------------------\nЗадача 4")
arr = [1, 2, 3, 5, 1, 5, 3, 10]
print(f"Неповторояющиеся элементы списка {arr} -> {get_uniq(arr)}")

# Экстра-задачи:

# 4 . Сумма квадратов первых десяти натуральных чисел равна
# 1^2 + 2^2 + ... + 10^2 = 385
# Квадрат суммы первых десяти натуральных чисел равен
# (1 + 2 + ... + 10)^2 = 552 = 3025
# Следовательно, разность между суммой квадратов и квадратом суммы первых десяти натуральных чисел составляет 3025 − 385 = 2640.
# Найдите разность между суммой квадратов и квадратом суммы первых ста натуральных чисел.
# S_n = n*(n+1)/2- сумма первых n натуральных чисел, S_n2 = n*(n+1)*(2 * n +1)/6 - сумма квадратов первых n натуральных чисел

# По формуле


def std(n):
    sum_n = n*(n+1)//2
    sum_n2 = n*(n+1)*(2*n + 1)//6

    return sum_n**2 - sum_n2

# Циклом


def std_2(n):
    sum_of_squares = sum([i**2 for i in range(1, n+1)])
    square_of_sum = sum([i for i in range(1, n+1)])**2

    return square_of_sum - sum_of_squares


print("-------------------------\nExtra задача 4")
N = 100
print(
    f"Разность между квадратом суммы и суммой квадратов первых {N} натуральных чисел = {std(N)}")

# 3 Начиная в вершине треугольника (см. пример ниже) и перемещаясь вниз на смежные числа, максимальная сумма до основания составляет 23.
# 3
# 7 4
# 2 4 6
# 8 5 9 3
# То есть, 3 + 7 + 4 + 9 = 23.
# Найдите максимальную сумму пути от вершины до основания следующего треугольника:
# 75
# 95 64
# 17 47 82
# 18 35 87 10
# 20 04 82 47 65
# 19 01 23 75 03 34
# 88 02 77 73 07 63 67
# 99 65 04 28 06 16 70 92
# 41 41 26 56 83 40 80 70 33
# 41 48 72 33 47 32 37 16 94 29
# 53 71 44 65 25 43 91 52 97 51 14
# 70 11 33 28 77 73 17 78 39 68 17 57
# 91 71 52 38 17 14 91 43 58 50 27 29 48
# 63 66 04 68 89 53 67 30 73 16 69 87 40 31
# 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

# Элементы треугольника хранятся в файле triangle_path. Строки файла соответсвуют строкам треугольника
triangle_file = 'triangle.txt'


def read_triangle(file_triangle: str) -> list:
    '''
    Метод считывает из файла file_triangle данные треугольника и возвращает
    массив с элементами треугольника
    '''
    with open(file_triangle, 'r') as tri:
        lines = tri.readlines()
        tri_arr = [[0 for _ in range(len(lines))] for _ in range(len(lines))]
        i = 0
        for line in lines:
            tr_raw = line.split()
            for j in range(len(tr_raw)):
                tri_arr[i][j] = int(tr_raw[j])
            i += 1
    return tri_arr


def max_path(list):
    summa = list[0][0]
    max_j = 0
    for r in range(len(list[0])-1):
        left = list[r + 1][max_j]
        right = list[r + 1][max_j + 1]
        max_val = max(left, right)
        max_j = max_j if max_val == left else max_j + 1
        summa += max_val
    return summa


def max_triangle_path(file_triangle):
    triangle_list = read_triangle(file_triangle)
    return max_path(triangle_list)


print("-------------------------\nExtra задача 3")
print(f"Максимальна сумма пути: {max_triangle_path(triangle_file)}")

# Extra 1
# Определите функцию, которая принимает римскую цифру в качестве аргумента
#  и возвращает ее значение в виде числового десятичного целого числа. Вам не нужно проверять форму римской цифры.
# Современные римские цифры записываются путем выражения каждой десятичной цифры числа,
# которое должно быть закодировано отдельно, начиная с самой левой цифры.
# Таким образом, 1990 отображается "MCMXC" (1000 = M, 900 = CM, 90 = XC),
# а 2008 отображается "MMVIII" (2000 = MM, 8 = VIII). 
# Римская цифра для 1666, "MDCLXVI", использует каждую букву в порядке убывания.
# Пример: имя_вашей_функции ('XXI') # должно вернуть 21


def rom_to_dec(rom: str) -> int:
    rom_dict = {"I": 1, "V": 5, "X": 10,
                "L": 50, "C": 100, "D": 500, "M": 1000}
    rom_str = rom.upper()
    decim_num = 0
    for i in range(len(rom_str)-1):
        cur_sym = rom_dict.get(rom_str[i])
        next_sym = rom_dict.get(rom_str[i+1])
        if cur_sym >= next_sym:
            decim_num += cur_sym
        elif cur_sym < next_sym and (next_sym // cur_sym <= 10):
            decim_num -= cur_sym
        i += 1
    decim_num += rom_dict.get(rom_str[len(rom_str)-1])

    return decim_num


rom_str = "MDCLXVI"
print("-------------------------\nExtra задача 1")
print(f"{rom_str} -> {rom_to_dec(rom_str)}")
