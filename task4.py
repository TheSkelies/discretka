
def nod(a, b): # 1
    if b > a:
        a, b = b, a

    if a % b == 0:
        return b

    return nod(b, a%b)

# функция из 1 задания

def nok(a, b): # 3
    return int(a*b/nod(a, b))

# функция из 3 задания

def nok_of_list(nums): # 4
    if len(nums) == 2:
        return nok(nums[0], nums[1])

    a = nums.pop()
    b = nums.pop()

    nums.append(nok(a, b))

    return nok_of_list(nums)

print(nok_of_list([12, 32, 36]))
