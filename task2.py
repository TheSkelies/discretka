def nod(a, b): # 1
    if b > a:
        a, b = b, a

    if a % b == 0:
        return b

    return nod(b, a%b)

# использовали функцию из 1 задания

def nod_of_list(nums): # 2

    if len(nums) == 2:
        return nod(nums[0], nums[1])

    a = nums.pop()
    b = nums.pop()

    nums.append(nod(a, b))

    return nod_of_list(nums)

print(nod_of_list([120, 72, 48]))
