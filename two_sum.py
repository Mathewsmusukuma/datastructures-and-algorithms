def two_sum(nums, target):

    log_dict = {}

    for idx, el in enumerate(nums):
        corresponding_el = target - el
        if(corresponding_el in log_dict):
            return [log_dict[corresponding_el], idx]
        else:
            log_dict[el] = idx
    