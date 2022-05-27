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

print(f"НОК({a},{b}) = {lcm(a, b)}")
