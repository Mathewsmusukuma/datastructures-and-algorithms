def find_element(cards, query):
    """
    1. Create  variable that will hold position set it to 0
    2. Check if the length of card is less than position 
    3.Check if the card position is equal to the query, 
    if true return position,,, element found. Otherwise, keep searching
    4. If there is no match, return -1
    
    """
    cards.sort()

    low, high = 0, len(cards) - 1
    while low <= high:
        mid = (low + high) // 2
        midle_number = cards[mid]

        if midle_number == query:
            return mid
        elif midle_number < query:
            low = midle_number + 1
        else:
            high = mid - 1
    return -1
