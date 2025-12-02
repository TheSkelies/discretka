
def nod(a, b): # 1
    if b > a:
        a, b = b, a

    if a % b == 0:
        return b

    return nod(b, a%b)

# функция из 1 задания

def nok(a, b): # 3
    return int(a*b/nod(a, b))

print(nok(8, 54))
