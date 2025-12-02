


def nod(a, b): # 1
    if b > a:
        a, b = b, a

    if a % b == 0:
        return b

    return nod(b, a%b)

print(nod(76764, 36))

def nod_of_list(nums): # 2

    if len(nums) == 2:
        return nod(nums[0], nums[1])

    a = nums.pop()
    b = nums.pop()

    nums.append(nod(a, b))

    return nod_of_list(nums)

print(nod_of_list([120, 72, 48]))

def nok(a, b): # 3
    return int(a*b/nod(a, b))

print(nok(8, 54))

def nok_of_list(nums): # 4
    if len(nums) == 2:
        return nok(nums[0], nums[1])

    a = nums.pop()
    b = nums.pop()

    nums.append(nok(a, b))

    return nok_of_list(nums)

print(nok_of_list([12, 32, 36]))


def resheto_eratosphena(a, b): # 5
    list_to_prime = [i for i in range(b+1)]
    list_to_prime[0] = list_to_prime[1] = -1

    for i in range(2, int(len(list_to_prime)**0.5) + 1):
        if list_to_prime[i] > 0:
            for j in range(i**2, len(list_to_prime), i):
                list_to_prime[j] = -1

    list_to_prime = [i for i in list_to_prime if i >= a]

    return list_to_prime


print(resheto_eratosphena(2, 100))


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


def lcg(x0):
    # конгруэнтный генератор указанного количества чисел (size) с заданными параметрами
    # и определённым начальным числом (x0)

    m = 6075
    a = 106
    c = 1283
    result = []  # массив для сгенерированных чисел в указанном количестве
    x = x0
    for i in range(3):
        x = (a * x + c) % m  # используем классическую формулу для конгруэнтного генератора
        result.append(x)
    return result


print(lcg(75)) # 3158 1906 2844


def rsa_encrypting(m):
    f, s = 5, 119
    # Шифрование: c = m^e mod n (encr = m**f % s)
    encr = m**f % s
    return encr


print(rsa_encrypting(854)) # 21


def rsa_decrypting(c):
    f, s = 77, 119

    # Дешифрование: m = c^d mod n (m = c**f % s)
    m = c**f % s
    return m

print(rsa_decrypting(534))
