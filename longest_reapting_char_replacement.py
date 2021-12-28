def char_replacement(s, k):
    count = {}
    results = 0
    left = 0
    max_frequence = 0
    
    for right in range(len(s)):
        count[s[right]] = 1 +count.get(s[right], 0)
        max_frequence = max(max_frequence, count[s[right]])

        while (right - left) - max_frequence > k:
            count[s[left]] -= 1
            left += 1
        results = max(results, right - left + 1)
    
    return results
