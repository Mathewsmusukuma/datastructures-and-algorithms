def length_of_longest_substring(string):
    charSet = set()
    left = 0
    results = 0
    for right in range(len(string)):
        while string[right] in charSet:
            charSet.remove(string[left])
            left += 1
        charSet.add(string[right])
        results = max(results, right - left + 1)
    return results
