from collections import Counter
def simCount(numbers):
    counts = Counter(numbers) # multiset of distinct values / count
    result = []
    for n in numbers:
        r = counts[n]-1 # duplicates
    for i,b in enumerate(n): # 1 bit changes
        r += counts[n[:i]+"01"[b=="0"]+n[i+1:]] # count others
        result.append(r) # sum of similars
    return result

A = ['100','110','010','011','100']
print(simCount(A)) # [2, 3, 2, 1, 2]