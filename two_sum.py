def two_sum(nums, target):
    hash_map = {}
    for index, value in enumerate(nums):
        diff = target - value
        if diff in hash_map:
            return [hash_map[diff], index]
        hash_map[value] = index
    return -1

print(two_sum([9,10,2,4,5,8,],19))
