def max_product(nums):
    result = max(nums)
    currentMin, currentMax = 1, 1

    for n in nums:            
        temp = currentMax * n
        currentMax = max(n * currentMax, n * currentMin, n)
        currentMin = min(temp, n * currentMin, n)
        result = max(result,currentMax)

    return result

