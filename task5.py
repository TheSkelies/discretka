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
