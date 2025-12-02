def nod(a, b): # 1
    if b > a:
        a, b = b, a

    if a % b == 0:
        return b

    return nod(b, a%b)

print(nod(76764, 36))
