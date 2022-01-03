def searchRange(nums, target):
        left = binarySearch(nums,target,True)
        right = binarySearch(nums,target,False)
        return [left,right]

def binarySearch(nums, target, leftBias):
    left, right = 0, len(nums) - 1
    i = -1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > target:
            right -= 1
        elif nums[mid] < target:
            left += 1
        else:
            i = mid
            if leftBias:
                right = mid -1
            else:
                left = mid + 1
    return i

arr = [1,2,3,4,5,6,7,8,9,10]
arr.sort()
print(searchRange(arr,9))