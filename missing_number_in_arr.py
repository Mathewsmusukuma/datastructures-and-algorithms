def find_missing_num(input):
    total_number_of_elements = sum(input)
    n = len(input) + 1
    actual_total = (n * (n + 1)) / 2
    return actual_total - total_number_of_elements
    