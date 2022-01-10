

def maxAlternatingSum(nums):
    sum_even, sum_old = 0,0
    
    for i in range(len(nums) -1,-1,-1):
        temp_even = max(sum_old + nums[i], sum_even)
        temp_old = max(sum_even - nums[i], sum_old)
        sum_even, sum_old = temp_even, temp_old
    return sum_even

print(maxAlternatingSum([2,4,-1,4])) # -> 9