def rsa_decrypting(c):
    f, s = 77, 119

    # Дешифрование: m = c^d mod n (m = c**f % s)
    m = c**f % s
    return m

print(rsa_decrypting(534))
