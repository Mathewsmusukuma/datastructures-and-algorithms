def romanToInt(s):
        mapped = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        ret = 0
        for index, char in enumerate(s):
            val = mapped[char]
            if index == len(s)-1:
                ret += val
                break
            next_val = mapped[s[index + 1]]
            if next_val > val:
                ret -= val
            else:
                ret += val
        return ret
