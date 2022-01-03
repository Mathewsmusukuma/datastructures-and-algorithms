from collections import defaultdict

def maxOperations(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    seen = defaultdict(int)
    answer = 0
    for num in nums:
        addend = k - num
        if seen[addend] >= 1:
            seen[addend] -= 1
            seen[num] -= 1
            answer += 1
            # We increment this afterward, to make sure it doesn't
            # break when addend = num
        seen[num] += 1
    return answer
