
def duplicate_num(nums):
    slow,fast, slow2 = 0,0,0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    while True:
        slow = nums[slow]
        slow2 = nums[slow2]
        if slow2 == slow:
            return slow
