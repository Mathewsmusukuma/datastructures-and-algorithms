def linear_search(list, target):
    """
    Returns the index position of the list if found
    else returns -1
    """
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return -1
    