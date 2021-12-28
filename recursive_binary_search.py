def recursive_binary_search(list, targe):
    list.sort() # Very important, else binary search won't work.
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list)) // 2

        if list[midpoint] == targe:
            return True
        elif list[midpoint] < targe:
            return recursive_binary_search(list[midpoint +1:], targe)
        else:
            return recursive_binary_search(list[:midpoint], targe)