def func(nums, num, position=0):
    nums.insert(position, num)
    return nums

print(func([1, 2, 3, 4, 5], 10, 4))
print(func([1, 2, 3, 4, 5], 10)) 