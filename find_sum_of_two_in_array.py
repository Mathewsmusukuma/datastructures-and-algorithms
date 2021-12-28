def find_sum_of_two(arr, val):
    found_values = set()
    for a in arr:
        if val - a in found_values:
            return True
        found_values.add(a)
    return False
