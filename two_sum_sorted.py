def two_sum_sorted(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        currentSum = nums[left] + nums[right]
        if currentSum > target:
            right -= 1
        elif currentSum < target:
            left += 1
        else:
            return [left, right]
    return[]

arr = [1,2,3,4,5,6,7,8,9,10]
arr.sort()
print(two_sum_sorted(arr,19))
