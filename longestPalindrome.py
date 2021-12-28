def logestPalindromeSub(s):    
    longestSubstring = ""

    for i in range(len(s)):
        center = expandAroundCenter(s,i,i)
        inBetween = expandAroundCenter(s, i, i + 1)
        
        longestSubstring = max(longestSubstring, center, inBetween, key=len)

    return longestSubstring


def expandAroundCenter(s, left, right):
    """"
    Helper function to expand the 
    search arround center of the string
    """
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1: right]
    