def extended_evklid(x, y):
    if x == 0:
        return y, 0, 1
    gcd, x1, y1 = extended_evklid(y % x, x)
    x_coef = y1 - (y // x) * x1
    y_coef = x1
    return gcd, x_coef, y_coef


def mod_division(a, b, n):
    # Приводим a и b к остаткам по модулю n
    a = a % n
    b = b % n

    # Находим НОД(b, n) и коэффициенты
    g, x, y = extended_evklid(b, n)

    # Находим обратный к b по модулю n
    b_inv = x % n

    # Вычисляем r = a * b^(-1) mod n
    r = (a * b_inv) % n

    return r

print(mod_division(43, 79, 131))
