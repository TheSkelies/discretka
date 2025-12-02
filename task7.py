def is_full_sqrt(n):
    # проверка, является ли число полным квадратом
    if n < 0:
        return False
    root = int(n**0.5)  # берём корень и округляем вниз
    return root * root == n  # проверяем является ли число полным квадратом


def is_prime(n):
    # проверка числа на простоту
    if n <= 1:  # все числа меньше 1 - не простые
        return False
    for i in range(2, int(n**0.5) + 1):  # проходим все числа от 2 до sqrt(n)
        if n % i == 0:  # проверяем деление на текущий делитель
            return False
    return True


def fermat_factorization(n):
    # факторизация Ферма (рекурсивная)
    if n == 1:  # если вводное число - 1, нет множетелей Ферма
        return []

    if n % 2 == 0:  # если число чётное
        return [2] + fermat_factorization(n // 2)  # один из делителей точно 2, дальше просчитываем все остальные

    if is_prime(n):  # если вводное число простое
        return [n]  # возвращаем его же, т.к. разложение закончено


    x = int(n**0.5) + 1 # берём такое число, что x^2 > n
    while not is_full_sqrt((x**2) - n): # пока число (x ^ 2 - n) не является полным квадратом
        x += 1 # прибавляем по единице
    # когда мы нашли такое число, у нас будет x^2 - n = y^2
    y = int((x**2 - n) ** 0.5) # берём корень из полученного уравнения
    a, b = x-y, x+y # два множителя - p и q

    return fermat_factorization(a) + fermat_factorization(b)



print(fermat_factorization(8))
