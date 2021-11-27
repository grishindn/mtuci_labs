import math


def calculation(x):
    t = math.log(math.sqrt(abs(x - 2)) + 1.2) / (2 + math.e**x) + (2 / x)**(1 / 3)
    return t


print("Введите Х: ")
x = float(input())
f = calculation(x)
print(f)
