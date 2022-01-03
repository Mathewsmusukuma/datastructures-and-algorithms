def binary_search(list, target):
    list.sort() 
    first_position = 0
    last_position = len(list) - 1

    while first_position <= last_position:
        mid = (last_position + first_position) // 2
        middle_point = list[mid]

        if middle_point == target:
            return mid
        elif middle_point < target:
            first_position = mid + 1
        else:
            last_position = mid - 1