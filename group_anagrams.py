from typing import DefaultDict


def group_anagrans(strs):
    # Mapping char count to list anagrams
    res = DefaultDict(list)

    for s in strs:
        count = [0] * 26 # count from a....z
        for char in s:
            count[ord(char) - ord('a')] += 1
        res[tuple(count)].append(s)
    
    return list(res.values())

print(group_anagrans(["eat","tea","tan","ate","nat","bat"]))
