
# Input: s = "anagram", t = "nagaram"
# Output: true
def isAnagram( s: str, t: str) -> bool:
    if len(s)!=len(t):
        return False
    d = {}
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for i in t:
        if i in d:
            d[i] -= 1
        else:
            return False
    for i,j in d.items():
        if j != 0:
            return False
    return True

s = "anagram"
t = "nagaram"
print(isAnagram(s,t))
