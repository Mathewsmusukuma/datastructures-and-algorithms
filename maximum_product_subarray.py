def max_product(nums):
    result = max(nums)
    currentMin, currentMax = 1, 1

    for n in nums:            
        temp = n * currentMax
        currentMin = min(temp, n * currentMin, n)
        currentMax = max(n * currentMax, n * currentMin, n)
        
        result = max(result,currentMax)

    return result

print(max_product([2,3,4,5,6,7,8]))