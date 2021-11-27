import math


def func(a, b, c, x):
    if x >= 3:
        if math.sqrt(x) > a:
            t = math.sqrt(x)
        else:
            t = a
    elif 0 <= x <= 3:
        t = math.cos(a + c * x**2 / b)
    else:
        if math.sqrt(a**2 + x) > math.tan(x - c**2):
            e1 = math.sqrt(a ** 2 + x)
        else:
            e1 = math.tan(x - c**2)
        if e1 < math.log(x**2 + c):
            t = e1
        else:
            t = math.log(x**2 + c)
    return t


