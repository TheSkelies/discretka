def rsa_encrypting(m):
    e, n = 5, 119
    # Шифрование: c = m^e mod n (encr = m**e % n)
    encr = m**e % n
    return encr


print(rsa_encrypting(854)) # 21
