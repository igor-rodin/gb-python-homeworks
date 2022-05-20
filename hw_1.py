# Задача 1
# Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д. (-3)**(N-1)

def gen_powers_of_three(num):
    return [(-3)**num for num in range(num)]


n = 5
print(gen_powers_of_three(n))
